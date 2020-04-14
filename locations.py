from DB import SQLite


class Locations(object):

    def __init__(self, location_id, title):
        self.location_id = location_id
        self.title = title

    def save(self):
        with SQLite() as db:
            db.execute(
                '''
                INSERT INTO locations
                VALUES (NULL, ?)
                ''', (self.title,))
            return self

    @staticmethod
    def all():
        with SQLite() as db:
            rows = db.execute('SELECT * FROM locations').fetchall()
            return [Locations(*row) for row in rows]

    @staticmethod
    def drop():
        with SQLite() as db:
            db.execute("DELETE FROM locations")
