from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

class PhoneBookForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    hero_name = StringField('Hero Name', validators=[DataRequired()])
    phone_num = StringField('Phone Number', validators=[DataRequired()])
    email_add = StringField('Email Address', validators=[DataRequired(), Email()])
    submit = SubmitField()