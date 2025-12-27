from flask_login import UserMixin
from cheesestick.database.database import Database

class User(UserMixin):
    def __init__(self, user_id: int, username: str, password_hash: str):
        self.id = str(user_id)
        self.username = username
        self.password_hash = password_hash

    @classmethod
    def get(cls, user_id: str):
        db = Database("CheeseStick.sqlite")
        row = db.cursor.execute(
            "SELECT id, username, password_hash FROM users WHERE id=?",
            (user_id,)
        ).fetchone()
        if row:
            return cls(*row)
        else:
            return None