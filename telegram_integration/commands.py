from telegram import Update, ParseMode
from telegram.ext import CallbackContext

import logger
from last_fm import message_for_random_loved_track, message_for_random_listened_artist
from storage.models import User, NoRegisteredUser
from telegram_integration import messages
from telegram_integration.messages import NO_USER_REGISTERED


def _send_message(update, context, text):
    context.bot.send_message(chat_id=update.message.chat_id, text=text,
                             parse_mode=ParseMode.MARKDOWN)


def help(update: Update, context: CallbackContext):
    logger.error("Sending help message")
    _send_message(update, context, text=messages.HELP)


def register_user(update: Update, context: CallbackContext):
    logger.error("Registering user")

    if len(context.args) != 1:
        _send_message(update, context, text="You should send your LastFM user!")
        return

    lastfm_user = context.args[0]
    message = User.register(lastfm_user=lastfm_user, telegram_id=update.message.from_user.id)
    _send_message(update, context, text=message)


def send_random_loved_track(update: Update, context: CallbackContext):
    logger.error("Sending random loved track")
    try:
        user = User.get(telegram_id=update.message.from_user.id)
    except NoRegisteredUser:
        message = NO_USER_REGISTERED
    else:
        message = message_for_random_loved_track(user=user)

    _send_message(update, context, text=message)


def send_random_listened_artist(update: Update, context: CallbackContext):
    logger.error("Sending random listened artist")
    try:
        user = User.get(telegram_id=update.message.from_user.id)
    except NoRegisteredUser:
        message = NO_USER_REGISTERED
    else:
        message = message_for_random_listened_artist(user=user)

    _send_message(update, context, text=message)


AVAILABLE_COMMANDS = (
    ("loved", send_random_loved_track), ("listened", send_random_listened_artist), ("register", register_user),
    ("help", help))
