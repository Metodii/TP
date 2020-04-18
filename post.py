from DB import SQLite


class Post(object):

    def __init__(self, post_id, title, image, size, price, bed_count, location_id, description):
        self.post_id = post_id
        self.title = title
        self.image = image
        self.size = size
        self.price = price
        self.bed_count = bed_count
        self.location_id = location_id
        self.description = description

    def save(self):
        with SQLite() as db:
            db.execute(
                '''
                INSERT INTO post 
                VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    self.title,
                    self.image,
                    self.size,
                    self.price,
                    self.bed_count,
                    self.location_id,
                    self.description))
            return self

    @staticmethod
    def all():
        with SQLite() as db:
            rows = db.execute('SELECT * FROM post').fetchall()
            return [Post(*row) for row in rows]
