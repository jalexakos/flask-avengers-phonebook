from aveng_pb import app, db

from datetime import datetime

class PhoneBook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)
    hero_name = db.Column(db.String(150))
    phone_num = db.Column(db.String(15), nullable=False)
    email_add = db.Column(db.String(150), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    def __init__(self,first_name,last_name,hero_name,phone_num,email_add,phonebook_id):
        self.first_name = first_name
        self.last_name = last_name
        self.hero_name = hero_name
        self.phone_num = phone_num
        self.email_add = email_add
        self.phonebook_id = phonebook_id
    
    def __repr__(self):
        return f'The hero entered here is {self.hero_name}. Welcome to the Avengers.'