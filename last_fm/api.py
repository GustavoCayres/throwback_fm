import os

import requests

import logger

API_ROOT = "http://ws.audioscrobbler.com/2.0/"
TRACKS_PER_PAGE = 1


def _params(method, **optional):
    return {
        "api_key": os.environ["LAST_FM_API_KEY"],
        "format": "json",
        "method": method,
        **optional
    }


def get(method, user, **kwargs):
    response = requests.get(API_ROOT, params=_params(method=method, user=user, **kwargs))
    try:
        response.raise_for_status()
    except Exception as e:
        logger.error(response.json())
        raise e

    return response.json()
