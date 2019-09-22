from math import ceil
from random import randrange

from last_fm import api

PERCENTAGE_OF_VALID_ARTISTS = .3


def total_artists():
    json = api.get(method="user.getTopArtists", limit=1)
    return int(json["topartists"]["@attr"]["total"])


class NoArtistsException(Exception):
    pass


def artist_index():
    n = total_artists()
    if n == 0:
        raise NoArtistsException

    return randrange(1, ceil(total_artists() * PERCENTAGE_OF_VALID_ARTISTS) + 1)


def get_random_artist():
    index = artist_index()
    json = api.get(method="user.getTopArtists", limit=1, page=index)
    return json["topartists"]["artist"][0]


def name(artist):
    return artist["name"]


def url(artist):
    return artist["url"]


def message_for_random_listened_artist():
    try:
        artist = get_random_artist()
    except NoArtistsException:
        return "It seems you haven't listened to anything yet..."

    return f"*Here's an artist you might like to remember:*\n[{name(artist)}]({url(artist)})"
