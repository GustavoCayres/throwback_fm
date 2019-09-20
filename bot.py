import os
import sys

from telegram.ext import Updater, CommandHandler

from telegram_integration.commands import AVAILABLE_COMMANDS


def main():
    updater = Updater(os.environ["BOT_TOKEN"], use_context=True)
    dp = updater.dispatcher
    for command in AVAILABLE_COMMANDS:
        dp.add_handler(CommandHandler(*command))

    updater.start_webhook(webhook_url="https://throwback-fm.herokuapp.com/")
    print("Pooling for chat messages and idling...", file=sys.stderr, flush=True)
    updater.idle()


if __name__ == '__main__':
    main()
