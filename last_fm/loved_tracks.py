import random

from . import api

TRACKS_PER_PAGE = 1


def random_track_index():
    json = api.get(method="user.getLovedTracks", limit=1)

    attributes = json["lovedtracks"]["@attr"]
    total_tracks = attributes["total"]
    return random.randint(1, int(total_tracks))


def get_random_loved_track():
    index = random_track_index()
    json = api.get(method="user.getLovedTracks", limit=1, page=index)

    track = json["lovedtracks"]["track"][0]

    return track


def name(track):
    return track["name"]


def artist_name(track):
    return track["artist"]["name"]


def artist_url(track):
    return track["artist"]["url"]


def url(track):
    return track["url"]


def message_for_random_loved_track():
    track = get_random_loved_track()
    return f"*Here's a track we think you'd like to remember:*\n[{name(track)}]({url(track)}) by [{artist_name(track)}]({artist_url(track)})"
