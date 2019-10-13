from sqlalchemy import Table, Column, String, Integer, MetaData

meta = MetaData()
users = Table('users', meta,
              Column('lastfm_user', String, nullable=False),
              Column('telegram_id', Integer, primary_key=True),
              Column('total_loved_tracks', Integer, nullable=False),
              Column('total_artists', Integer, nullable=False)
              )
