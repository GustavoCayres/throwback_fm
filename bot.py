import os
import sys

from telegram.ext import Updater, CommandHandler

from commands import available_commands
from heroku import keep_alive


def main():
    updater = Updater(os.environ["BOT_TOKEN"], use_context=True)
    dp = updater.dispatcher
    for command in available_commands:
        dp.add_handler(CommandHandler(*command))

    updater.start_polling()
    print("Pooling for chat messages and idling...", file=sys.stderr, flush=True)

    port = os.getenv("PORT")
    if port is None:
        updater.idle()
    else:
        keep_alive(os.environ["HEROKU_APP_URL"], port)


if __name__ == '__main__':
    main()
