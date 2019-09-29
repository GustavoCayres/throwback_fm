from math import ceil
from random import randrange

from last_fm import api
from telegram_integration import messages

PERCENTAGE_OF_VALID_ARTISTS = .3


def artist_index(user):
    n = api.get_total_artists(user)
    if n == 0:
        raise api.NoArtistsException

    return randrange(1, ceil(n * PERCENTAGE_OF_VALID_ARTISTS) + 1)


def get_random_artist(user):
    index = artist_index(user)
    return api.get_top_artist(user, index)


def name(artist):
    return artist["name"]


def url(artist):
    return artist["url"]


def message_for_random_listened_artist(user):
    try:
        artist = get_random_artist(user)
    except api.NoArtistsException:
        return messages.NEVER_LISTENED_TO_A_TRACK

    return messages.LISTENED_ARTIST(name(artist), url(artist))
