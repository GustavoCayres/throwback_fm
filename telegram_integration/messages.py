from telegram import ParseMode


def send_message(update, context, text):
    context.bot.send_message(chat_id=update.message.chat_id, text=text,
                             parse_mode=ParseMode.MARKDOWN)
