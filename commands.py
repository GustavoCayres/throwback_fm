from telegram import Update
from telegram.ext import CallbackContext

from last_fm import message_for_random_loved_track


def _send_random_loved_song(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.message.chat_id, text=message_for_random_loved_track())


available_commands = (("loved", _send_random_loved_song),)
