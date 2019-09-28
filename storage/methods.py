from sqlalchemy.exc import IntegrityError

import logger
from storage.engine import db_engine
from storage.tables import users


def register(lastfm_name, telegram_name):
    with db_engine.connect() as conn:
        try:
            statement = users.insert().values(lastfm_name=lastfm_name, telegram_name=telegram_name)
        except IntegrityError:
            statement = users.update().where(telegram_name=telegram_name).values(lastfm_name=lastfm_name)

        conn.execute(statement)


def get_lastfm_user(telegram_user_id):
    with db_engine.connect() as conn:

        statement = users.select().where(users.c.telegram_name == str(telegram_user_id))

        lastfm_users = list(conn.execute(statement))
        if len(lastfm_users) != 1:
            return None

        return lastfm_users[0][0]
