from DB import SQLite

class Post(object):

    def __init__(self, post_id, title, image, location_id, size, price, bed_count, description):
        self.post_id = post_id
        self.title = title
        self.image = image
        self.location_id = location_id
        self.size = size
        self.price = price
        self.bed_count = bed_count
        self.description = description      
        
    def save(self):
        with SQLite() as db:
            db.execute(
                '''
                INSERT INTO post 
                VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)
                ''',(
                    self.title,
                    self.image,
                    self.location_id,
                    self.size,
                    self.price,
                    self.bed_count,
                    self.description))
            return self

