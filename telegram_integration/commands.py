from telegram import Update, ParseMode
from telegram.ext import CallbackContext

import logger
import storage
from last_fm import message_for_random_loved_track, message_for_random_listened_artist
from telegram_integration.messages import send_message


def register_user(update: Update, context: CallbackContext):
    logger.error("Registering user")

    if len(context.args) != 1:
        context.bot.send_message(chat_id=update.message.chat_id, text="You should send your LastFM user!",
                                 parse_mode=ParseMode.MARKDOWN)
        return

    lastfm_user = context.args[0]
    storage.register(lastfm_user=lastfm_user, telegram_id=update.message.from_user.id)
    send_message(update, context, text=f"LastFM user {lastfm_user} registered successfully")


def send_random_loved_track(update: Update, context: CallbackContext):
    logger.error("Sending random loved track")
    lastfm_user = storage.get_lastfm_user(telegram_id=update.message.from_user.id)

    context.bot.send_message(chat_id=update.message.chat_id, text=message_for_random_loved_track(user=lastfm_user),
                             parse_mode=ParseMode.MARKDOWN)


def send_random_listened_artist(update: Update, context: CallbackContext):
    logger.error("Sending random listened artist")
    lastfm_user = storage.get_lastfm_user(telegram_id=update.message.from_user.id)
    context.bot.send_message(chat_id=update.message.chat_id, text=message_for_random_listened_artist(user=lastfm_user),
                             parse_mode=ParseMode.MARKDOWN)


AVAILABLE_COMMANDS = (
    ("loved", send_random_loved_track), ("listened", send_random_listened_artist), ("register", register_user))
