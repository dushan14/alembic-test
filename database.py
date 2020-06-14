from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import ACTIVATED_CONFIG

engine = create_engine(ACTIVATED_CONFIG.DATABASE_URI, echo=ACTIVATED_CONFIG.LOG_SQL, connect_args={}, )
DatabaseSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


@contextmanager
def get_db_session():
    s = DatabaseSession()
    try:
        yield s
    finally:
        s.close()


# import models here to be identified by alembic
from model.book import Book
from model.user import User
