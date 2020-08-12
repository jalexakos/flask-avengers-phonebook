from aveng_pb import app, db, Message, mail
from flask import render_template, request, redirect, url_for
from aveng_pb.forms import PhoneBookForm, LoginForm
from aveng_pb.models import PhoneBook, check_password_hash
from flask_login import login_required, login_user, current_user, logout_user

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
        password = form.password.data
        print('\n', first_name, last_name, hero_name, phone_num, email_add)
        contact = PhoneBook(first_name,last_name,hero_name,phone_num,email_add,password)
        db.session.add(contact)
        db.session.commit()

        # Email Sender
        msg = Message(f'Thanks for signing up, {hero_name}!', recipients=[email_add])
        msg.body = ('Welcome to the Avengers!')
        msg.html = (f'<h1>Welcome to the Avengers, {hero_name}.' '<p>Now you can help us save the world!</p>')

        mail.send(msg)

    return render_template('phone_book.html', form=form)

# Login Page
@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        email = form.email.data
        password = form.password.data
        logged_user = PhoneBook.query.filter(PhoneBook.email_add == email).first()
        if logged_user and check_password_hash(logged_user.password, password):
            login_user(logged_user)
            return redirect(url_for('home'))
        else:
            return redirect(url_for('login'))
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))