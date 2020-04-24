from DB import SQLite

class User:
    def __init__(self, user_id, email, password):
        self.user_id = user_id
        self.email = email
        self.password = password

    def create(self):
        with SQLite() as db:
            db.execute('''
                INSERT INTO user (email, password)
                VALUES (?, ?)''', (self.email, self.password))
            return self

    @staticmethod
    def find_by_email(email):
        if not email:
            return None
        with SQLite() as db:
            row = db.execute(
                'SELECT * FROM user WHERE email = ?',
                (email,)
            ).fetchone()
            if row:
                return User(*row)