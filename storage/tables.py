from sqlalchemy import Table, Column, String, MetaData, Integer

from storage.engine import db_engine

meta = MetaData(db_engine)
users = Table('users', meta,
              Column('lastfm_user', String),
              Column('telegram_id', Integer, primary_key=True)
              )
