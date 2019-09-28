import sys

from telegram import Update, ParseMode
from telegram.ext import CallbackContext

from last_fm import message_for_random_loved_track, message_for_random_listened_artist


def send_random_loved_track(update: Update, context: CallbackContext):
    print("Sending random loved track", file=sys.stderr, flush=True)
    context.bot.send_message(chat_id=update.message.chat_id, text=message_for_random_loved_track(),
                             parse_mode=ParseMode.MARKDOWN)


def send_random_listened_artist(update: Update, context: CallbackContext):
    print("Sending random listened artist", file=sys.stderr, flush=True)
    context.bot.send_message(chat_id=update.message.chat_id, text=message_for_random_listened_artist(),
                             parse_mode=ParseMode.MARKDOWN)


AVAILABLE_COMMANDS = (("loved", send_random_loved_track), ("listened", send_random_listened_artist))
