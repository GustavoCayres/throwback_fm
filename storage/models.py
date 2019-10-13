from sqlalchemy import Table, Column, String, Integer, MetaData
from sqlalchemy.exc import IntegrityError

from last_fm import api
from storage.engine import db_engine

meta = MetaData()


class NoRegisteredUser(Exception):
    pass


class User:
    table = Table('users', meta,
                  Column('lastfm_user', String, nullable=False),
                  Column('telegram_id', Integer, primary_key=True),
                  Column('total_loved_tracks', Integer, nullable=False),
                  Column('total_artists', Integer, nullable=False)
                  )

    def __init__(self, lastfm_user, telegram_id, total_loved_tracks, total_artists):
        self.total_loved_tracks = total_loved_tracks
        self.telegram_id = telegram_id
        self.total_artists = total_artists
        self.lastfm_user = lastfm_user

    @classmethod
    def get(cls, telegram_id):
        with db_engine.connect() as conn:
            statement = cls.table.select().where(cls.table.c.telegram_id == telegram_id)

            users = list(conn.execute(statement))
            if len(users) == 0:
                raise NoRegisteredUser
            user = users[0]
            return cls(*user)

    @classmethod
    def register(cls, lastfm_user, telegram_id):
        try:
            total_artists = api.get_total_artists(lastfm_user)
            total_loved_tracks = api.get_total_loved_tracks(lastfm_user)
        except api.UserNotFound:
            return f"Wrong LastFM user"

        with db_engine.connect() as conn:
            try:
                statement = cls.table.insert().values(lastfm_user=lastfm_user, telegram_id=telegram_id,
                                                      total_artists=total_artists,
                                                      total_loved_tracks=total_loved_tracks)
                conn.execute(statement)
            except IntegrityError:
                statement = cls.table.update().where(cls.table.c.telegram_id == telegram_id).values(
                    lastfm_user=lastfm_user,
                    total_artists=total_artists,
                    total_loved_tracks=total_loved_tracks
                )
                conn.execute(statement)

        return f"LastFM user {lastfm_user} registered successfully"

    def save(self):
        with db_engine.connect() as conn:
            statement = self.table.update().where(self.table.c.telegram_id == self.telegram_id).values(
                lastfm_user=self.lastfm_user,
                total_artists=self.total_artists,
                total_loved_tracks=self.total_loved_tracks
            )
            conn.execute(statement)
