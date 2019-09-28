from sqlalchemy.exc import IntegrityError

from storage.engine import db_engine
from storage.tables import users

with db_engine.connect() as conn:
    try:
        users.create()
    except IntegrityError:
        pass
