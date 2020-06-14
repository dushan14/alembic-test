from sqlalchemy import Column, Integer, String, Boolean

from database import Base


class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(50), unique=True)
    is_active = Column(Boolean, default=True)
    name = Column(String(100), default=True)
    author = Column(String(100), default=True)