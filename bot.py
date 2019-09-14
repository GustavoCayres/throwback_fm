import os

from telegram.ext import Updater, CommandHandler

from commands import available_commands


def main():
    updater = Updater(os.environ["BOT_TOKEN"], use_context=True)
    dp = updater.dispatcher
    for command in available_commands:
        dp.add_handler(CommandHandler(*command))

    port = os.getenv("PORT")
    if port:
        print(f"Will start HTTP server at port {port}")
        updater.start_webhook(port=port)
    else:
        updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
