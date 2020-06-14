from sqlalchemy.orm import Session

import model
from database import get_db_session
from model.user import User


def add_some_users():
    with get_db_session() as s:
        user1 = User(name="Lol Man", email="lol@losdsdsdsdlosasa00dsds.com")
        s.add(user1)
        s.commit()
        print("user added")


def read_all_users():
    with get_db_session() as s:
        users = s.query(model.user.User).all()
        print(*users, sep="\n")


if __name__ == "__main__":
    add_some_users()
    read_all_users()
