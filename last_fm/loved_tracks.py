import random

from . import api

TRACKS_PER_PAGE = 1


def random_track_index(user):
    total_loved_tracks = api.get_total_loved_tracks(user=user)
    if total_loved_tracks == 0:
        raise api.NoLovedTracks

    return random.randint(1, total_loved_tracks)


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
    try:
        track = get_random_loved_track(user)
    except api.NoLovedTracks:
        return "You never loved a song!"
    return f"*Here's a track we think you'd like to remember:*\n[{name(track)}]({url(track)}) by [{artist_name(track)}]({artist_url(track)})"
