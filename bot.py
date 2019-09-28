import os
import sys

from telegram.ext import Updater, CommandHandler

from telegram.commands import AVAILABLE_COMMANDS


def main():
    updater = Updater(os.environ["BOT_TOKEN"], use_context=True)
    dp = updater.dispatcher
    for command in AVAILABLE_COMMANDS:
        dp.add_handler(CommandHandler(*command))

    print("Pooling for chat messages and idling...", file=sys.stderr, flush=True)

    environment = os.environ["ENVIRONMENT"]
    if environment == "DEVELOPMENT":
        updater.start_polling()
    elif environment == "HEROKU":
        updater.start_webhook(listen="0.0.0.0",
                              port=os.environ["PORT"],
                              url_path=os.environ["BOT_TOKEN"])
        updater.bot.set_webhook(F"{os.environ['HEROKU_APP_URL']}{os.environ['BOT_TOKEN']}")
    else:
        raise Exception(f"Unknown environment {environment}")

    updater.idle()


if __name__ == '__main__':
    main()
