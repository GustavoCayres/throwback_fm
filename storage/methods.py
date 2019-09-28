from sqlalchemy.exc import IntegrityError

from storage.engine import db_engine
from storage.tables import users


def register(lastfm_user, telegram_id):
    with db_engine.connect() as conn:
        try:
            statement = users.insert().values(lastfm_user=lastfm_user, telegram_id=telegram_id)
        except IntegrityError:
            statement = users.update().where(telegram_id=telegram_id).values(lastfm_user=lastfm_user)

        conn.execute(statement)


def get_lastfm_user(telegram_id):
    with db_engine.connect() as conn:

        statement = users.select().where(users.c.telegram_id == telegram_id)

        lastfm_users = list(conn.execute(statement))
        if len(lastfm_users) != 1:
            return None

        return lastfm_users[0][0]
