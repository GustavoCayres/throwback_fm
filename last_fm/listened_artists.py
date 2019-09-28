from math import ceil
from random import randrange

from last_fm import api

PERCENTAGE_OF_VALID_ARTISTS = .3


def total_artists(user):
    json = api.get(user=user, method="user.getTopArtists", limit=1)
    return int(json["topartists"]["@attr"]["total"])


class NoArtistsException(Exception):
    pass


def artist_index(user):
    n = total_artists(user)
    if n == 0:
        raise NoArtistsException

    return randrange(1, ceil(n * PERCENTAGE_OF_VALID_ARTISTS) + 1)


def get_random_artist(user):
    index = artist_index(user)
    json = api.get(user=user, method="user.getTopArtists", limit=1, page=index)
    return json["topartists"]["artist"][0]


def name(artist):
    return artist["name"]


def url(artist):
    return artist["url"]


def message_for_random_listened_artist(user):
    try:
        artist = get_random_artist(user)
    except NoArtistsException:
        return "It seems you haven't listened to anything yet..."

    return f"*Here's an artist you might like to remember:*\n[{name(artist)}]({url(artist)})"
