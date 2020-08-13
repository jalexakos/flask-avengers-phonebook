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
@login_required
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

# Contact Info Page
@app.route('/contact-info')
@login_required
def contact_info():
    contacts = PhoneBook.query.all()
    return render_template('contact-info.html', contacts=contacts)

# Retrieving Contact Info Page
@app.route('/contact-details/<int:phonebook_id>')
@login_required
def contact_detail(phonebook_id):
    contact_det = PhoneBook.query.get_or_404(phonebook_id)
    return render_template('contact-details.html',contact_det=contact_det)

# Updating Contact Info 
@app.route('/contact-details/update/<int:phonebook_id>', methods=['GET','POST'])
@login_required
def contact_update(phonebook_id):
    contact_det = PhoneBook.query.get_or_404(phonebook_id)
    update_det = PhoneBookForm()

    if request.method == 'POST' and update_det.validate():
        hero_name = update_det.hero_name.data
        phone_num = update_det.phone_num.data
        email_add = update_det.email_add.data
        user_id = current_user.id

        contact_det.hero_name = hero_name
        contact_det.phone_num = phone_num
        contact_det.email_add = email_add
        contact_det.phonebook_id = user_id

        db.session.commit()
        return redirect(url_for('contact_update', phonebook_id=phonebook_id))
    
    return render_template('contact_update.html', update_det=update_det)

# Deleting Contact Info
@app.route('/contact-details/delete/<int:phonebook_id>', methods=['POST'])
@login_required
def contact_delete(phonebook_id):
    contact_det = PhoneBook.query.get_or_404(phonebook_id)
    db.session.delete(contact_det)
    db.session.commit()
    return redirect(url_for('home'))

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