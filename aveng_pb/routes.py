from aveng_pb import app
from flask import render_template, request
from aveng_pb.forms import PhoneBookForm

# Home Page
@app.route('/')
def home():
    return render_template("home.html")

# Phone Book Entry Page
@app.route('/phone-book', methods=['GET','POST'])
def phone_book():
    form = PhoneBookForm()
    if request.method == 'POST' and form.validate():
        first_name = form.first_name.data
        last_name = form.last_name.data
        hero_name = form.hero_name.data
        phone_num = form.phone_num.data
        email_add = form.email_add.data
        print('\n', first_name, last_name, hero_name, phone_num, email_add)
    return render_template('phone_book.html', form=form)