from sqlalchemy.exc import IntegrityError

from last_fm import api
from storage.engine import db_engine
from storage.tables import users


class NoRegisteredUser(Exception):
    pass


def register(lastfm_user, telegram_id):
    try:
        total_artists = api.get_total_artists(lastfm_user)
        total_loved_tracks = api.get_total_loved_tracks(lastfm_user)
    except api.UserNotFound:
        return f"Wrong LastFM user"

    with db_engine.connect() as conn:
        try:
            statement = users.insert().values(lastfm_user=lastfm_user, telegram_id=telegram_id,
                                              total_artists=total_artists, total_loved_tracks=total_loved_tracks)
        except IntegrityError:
            statement = users.update().where(telegram_id=telegram_id).values(lastfm_user=lastfm_user,
                                                                             total_artists=total_artists,
                                                                             total_loved_tracks=total_loved_tracks)

        conn.execute(statement)

    return f"LastFM user {lastfm_user} registered successfully"


def get_lastfm_user(telegram_id):
    with db_engine.connect() as conn:
        statement = users.select().where(users.c.telegram_id == telegram_id)

        lastfm_users = list(conn.execute(statement))
        if len(lastfm_users) == 0:
            raise NoRegisteredUser

        return lastfm_users[0][0]
