import random

from . import api

TRACKS_PER_PAGE = 1


def random_track_index(user):
    return random.randint(1, api.get_total_loved_tracks(user=user))


def get_random_loved_track(user):
    index = random_track_index(user)

    return api.get_loved_track(user, index)


def name(track):
    return track["name"]


def artist_name(track):
    return track["artist"]["name"]


def artist_url(track):
    return track["artist"]["url"]


def url(track):
    return track["url"]


def message_for_random_loved_track(user):
    track = get_random_loved_track(user)
    return f"*Here's a track we think you'd like to remember:*\n[{name(track)}]({url(track)}) by [{artist_name(track)}]({artist_url(track)})"
