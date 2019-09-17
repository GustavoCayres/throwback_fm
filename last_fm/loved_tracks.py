import os
import random

import requests

API_ROOT = "http://ws.audioscrobbler.com/2.0/"
TRACKS_PER_PAGE = 1


def get_params(method, **optional):
    return {
        "api_key": os.environ["LAST_FM_API_KEY"],
        "format": "json",
        "method": method,
        **optional
    }


def random_track_index():
    response = requests.get(API_ROOT, params=get_params(method="user.getLovedTracks", user="danrawr_", limit=1))
    response.raise_for_status()

    json = response.json()

    attributes = json["lovedtracks"]["@attr"]
    total_tracks = attributes["total"]
    return random.randint(1, int(total_tracks))


def get_random_loved_track():
    index = random_track_index()
    response = requests.get(API_ROOT,
                            params=get_params(method="user.getLovedTracks", user="danrawr_", limit=1, page=index))
    json = response.json()

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
