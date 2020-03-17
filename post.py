from database import SQLite

class Post(object):

    def __init__(self, title, location_id, price, bed_count, description):
        self.title = title
        self.location_id = location_id
        self.price = price
        self.bed_count = bed_count
        self.descriptin = description      
        

