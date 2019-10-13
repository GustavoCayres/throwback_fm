import random

import logger
from telegram_integration import messages
from . import api

TRACKS_PER_PAGE = 1


def random_track_index(user):
    total_loved_tracks = api.get_total_loved_tracks(user=user)
    logger.error(total_loved_tracks)

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
        return messages.NEVER_LOVED_A_TRACK

    return messages.LOVED_TRACK(name(track), url(track), artist_name(track), artist_url(track))
