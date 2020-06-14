from database import get_db_session
from model.user import User


def add_some_users():
    with get_db_session() as s:
        user1 = User(name="Lol Man", email="lol@losdsdlo00dsds.com")
        s.add(user1)
        s.commit()
        print("added user1")


if __name__ == "__main__":
    add_some_users()
