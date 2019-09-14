import os
import socket

from telegram.ext import Updater, CommandHandler

from commands import available_commands


def main():
    updater = Updater(os.environ["BOT_TOKEN"], use_context=True)
    dp = updater.dispatcher
    for command in available_commands:
        dp.add_handler(CommandHandler(*command))

    updater.start_polling()
    try:
        port = os.environ["PORT"]
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("127.0.0.1", int(port)))
    except KeyError:
        pass

    updater.idle()


if __name__ == '__main__':
    main()
