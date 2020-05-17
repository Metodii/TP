from DB import SQLite
import datetime

class Post(object):

    def __init__(self, post_id, title, image, size, price, bed_count, location_id, available_from, available_to, description, user_id):
        self.post_id = post_id
        self.title = title
        self.image = image
        self.size = size
        self.price = price
        self.bed_count = bed_count
        self.location_id = location_id
        self.available_from = available_from
        self.available_to = available_to
        self.description = description
        self.user_id = user_id

    def save(self):
        with SQLite() as db:
            db.execute(
                '''
                INSERT INTO post 
                VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    self.title,
                    self.image,
                    self.size,
                    self.price,
                    self.bed_count,
                    self.location_id,
                    self.available_from,
                    self.available_to,
                    self.description,
                    self.user_id))
            return self

    @staticmethod
    def all(available_from=None, available_to=None):
        with SQLite() as db:
            rows = db.execute('SELECT * FROM post').fetchall()
            if available_from=="undefined":
                available_from=None

            if available_to=="undefined":
                available_to=None

            if not available_from or not available_to:
                return [Post(*row) for row in rows]

            return [Post(*row) for row in rows if (
                datetime.datetime.strptime(row[7], "%Y-%m-%d").date() < datetime.datetime.strptime(available_from, "%Y-%m-%d").date() and
                datetime.datetime.strptime(row[8], "%Y-%m-%d").date() > datetime.datetime.strptime(available_to, "%Y-%m-%d").date())]
