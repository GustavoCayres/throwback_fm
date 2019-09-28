from sqlalchemy.exc import IntegrityError

from storage.engine import db_engine
from storage.tables import users


def register(lastfm_name, telegram_name):
    with db_engine.connect() as conn:
        try:
            statement = users.insert().values(lastfm_name=lastfm_name, telegram_name=telegram_name)
        except IntegrityError:
            statement = users.update().where(telegram_name=telegram_name).values(lastfm_name=lastfm_name)

        conn.execute(statement)
