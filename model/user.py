from sqlalchemy import Column, Integer, String, Boolean

from database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    email = Column(String(100), unique=False, index=True)
    is_active = Column(Boolean, default=True)
    name = Column(String(100), default=True)
    age = Column(Integer, default=0)

    def __repr__(self):
        return "User [ id='{}', email='{}', is_active={}, nane={}, age={} ]" \
            .format(self.id, self.email, self.is_active, self.name, self.age)
