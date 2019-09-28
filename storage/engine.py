import os

from sqlalchemy import create_engine


db_engine = create_engine(os.environ["DATABASE_URL"])
