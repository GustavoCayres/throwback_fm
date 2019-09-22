import os
import sys


def debug(*args):
    if os.environ["ENVIRONMENT"] != "DEVELOPMENT":
        return

    print(*args, file=sys.stderr, flush=True)


def error(*args):
    print(*args, file=sys.stderr, flush=True)
