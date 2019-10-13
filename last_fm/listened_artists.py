from math import ceil
from random import randrange

from last_fm import api
from telegram_integration import messages

PERCENTAGE_OF_VALID_ARTISTS = .3


def artist_index(user):
    total_artists = user.total_artists
    if total_artists == 0:
        raise api.NoArtistsException

    return randrange(1, ceil(total_artists * PERCENTAGE_OF_VALID_ARTISTS) + 1)


def get_random_artist(user):
    index = artist_index(user)
    artist, total = api.get_top_artist(user.lastfm_user, index, with_total=True)
    user.total_artists = total
    user.save()

    return artist


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
