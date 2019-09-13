import os
import random

import requests

API_ROOT = "http://ws.audioscrobbler.com/2.0/"


def get_params(method, **optional):
    return {
        "api_key": os.environ["LAST_FM_API_KEY"],
        "format": "json",
        "method": method,
        **optional
    }


def get_loved_tracks():
    response = requests.get(API_ROOT, params=get_params(method="user.getLovedTracks", user="danrawr_"))
    response.raise_for_status()

    json = response.json()
    tracks = json["lovedtracks"]["track"]
    return tracks


def get_random_loved_track():
    tracks = get_loved_tracks()
    random_index = random.randrange(len(tracks))

    return tracks[random_index]


def name(track):
    return track["name"]


def artist_name(track):
    return track["artist"]["name"]


def url(track):
    return track["url"]


def message_for_random_loved_track():
    track = get_random_loved_track()
    return f"Listen to {name(track)} by {artist_name(track)}\n{url(track)}"
