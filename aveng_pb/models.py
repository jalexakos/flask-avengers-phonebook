from aveng_pb import app, db, login

# Import for Werkzeug Security - this is Flask
from werkzeug.security import generate_password_hash, check_password_hash

from datetime import datetime

# Imports for User Mixin
from flask_login import UserMixin

@login.user_loader
def load_user(phonebook_id):
    return PhoneBook.query.get(int(phonebook_id))

class PhoneBook(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)
    hero_name = db.Column(db.String(150), nullable=True)
    phone_num = db.Column(db.String(15), nullable=False)
    email_add = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(256), nullable=True)

    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    def __init__(self,first_name,last_name,hero_name,phone_num,email_add, password):
        self.first_name = first_name
        self.last_name = last_name
        self.hero_name = hero_name
        self.phone_num = phone_num
        self.email_add = email_add
        self.password = self.set_password(password)
    
    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def __repr__(self):
        return f'The hero entered here is {self.hero_name}. Welcome to the Avengers.'