import os

import requests

import logger

API_ROOT = "http://ws.audioscrobbler.com/2.0/"
TRACKS_PER_PAGE = 1


class NoArtistsException(Exception):
    pass


class NoLovedTracks(Exception):
    pass


class UserNotFound(Exception):
    pass


def _params(method, **optional):
    return {
        "api_key": os.environ["LAST_FM_API_KEY"],
        "format": "json",
        "method": method,
        **optional
    }


def _get(method, user, **kwargs):
    response = requests.get(API_ROOT, params=_params(method=method, user=user, **kwargs))
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            raise UserNotFound

        logger.error(response.json())
        raise e

    return response.json()


def get_top_artist(user, index):
    json = _get(user=user, method="user.getTopArtists", limit=1, page=index)
    return json["topartists"]["artist"][0]


def get_total_artists(user):
    json = _get(user=user, method="user.getTopArtists", limit=1)
    return int(json["topartists"]["@attr"]["total"])


def get_total_loved_tracks(user):
    json = _get(user=user, method="user.getLovedTracks", limit=1)

    return int(json["lovedtracks"]["@attr"]["total"])


def get_loved_track(user, index):
    json = _get(user=user, method="user.getLovedTracks", limit=1, page=index)

    return json["lovedtracks"]["track"][0]
