from database import SQLite

class User(object):

    def __init__(self, username, password, user_id=None):
        self.id = user_id
        self.username = username
        self.password = password

    def to_dict(self):
        user_data = self.__dict__
        del user_data["password"]
        return user_data

    def save(self):
        with SQLite() as db:
            cursor = db.execute(self.__get_save_query())
            self.id = cursor.lastrowid
        return self

    
