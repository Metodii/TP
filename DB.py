import sqlite3 as sqlite


DB_NAME = "onlineBooking.db"

conn = sqlite.connect(DB_NAME)

conn.cursor().execute('''
CREATE TABLE IF NOT EXISTS post
    (
 
        post_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        image BLOB NOT NULL,
        size TEXT NOT NULL,
        price TEXT NOT NULL,
        bed_count TEXT NOT NULL,
		location_id TEXT NOT NULL,
		description TEXT NOT NULL
    )
''')
conn.commit()

conn.cursor().execute('''
CREATE TABLE IF NOT EXISTS locations
    (
        location_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL
    )
''')
conn.commit()


conn.cursor().execute('''
CREATE TABLE IF NOT EXISTS user
    (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        address TEXT NOT NULL,
        phone_number TEXT NOT NULL UNIQUE
    )
''')
conn.commit()


class SQLite(object):
    def __enter__(self):
        self.conn = sqlite.connect(DB_NAME)
        return self.conn.cursor()

    def __exit__(self, type, value, traceback):
        self.conn.commit()
