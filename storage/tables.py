from sqlalchemy import Table, Column, String, MetaData

from storage.engine import db_engine

meta = MetaData(db_engine)
users = Table('users', meta,
              Column('lastfm_name', String),
              Column('telegram_name', String, primary_key=True)
              )
