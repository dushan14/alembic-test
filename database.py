from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import ACTIVATED_CONFIG

engine = create_engine(
    ACTIVATED_CONFIG.DATABASE_URI, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# import models here to be identified by alembic
from model.book import Book
from model.user import User
