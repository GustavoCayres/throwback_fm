from sqlalchemy import Table, Column, String, MetaData, Integer

meta = MetaData()
users = Table('users', meta,
              Column('lastfm_user', String),
              Column('telegram_id', Integer, primary_key=True),
              Column('total_loved_tracks', Integer),
              Column('total_artists', Integer)
              )


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    users.create()


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    users.drop()
