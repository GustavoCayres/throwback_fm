from storage.engine import db_engine
from storage.tables import users

with db_engine.connect() as conn:
    users.create()
