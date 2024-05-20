'''
Project 3: Zoo Web App
Flask Routes
Authors:
    Kyler Kramer
    Sho Vang
'''

import bcrypt
from flask_login import login_required, login_user, logout_user, current_user
from flask_wtf import FlaskForm
from werkzeug.utils import secure_filename
from flask import Flask, redirect, render_template
from flask import url_for, flash, request, session
from app.forms import AnimalForm, LoginForm, SignUpForm, ChangePWForm
from app.models import User, Animal
from app import app, db
import os
import uuid
from sqlalchemy import func


@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(name=form.name.data).first()
        if existing_user:
            flash("User exists, please log in")
            return redirect(url_for('login'))

        if form.passwd.data == form.passwd_confirm.data:
            hashed_pw = bcrypt.hashpw(form.passwd.data.encode(
                'utf-8'), bcrypt.gensalt())
            hashed_challenge = bcrypt.hashpw(
                form.challenge.data.encode('utf-8'), bcrypt.gensalt())
            new_user = User(
                id=form.id.data,
                phoneNumber=form.phoneNumber.data,
                name=form.name.data,
                passwd=hashed_pw,
                membership=form.membership.data,
                challenge=hashed_challenge
            )
            db.session.add(new_user)
            db.session.commit()
            flash('Signed up successfully!')
            return redirect(url_for('login'))
    return render_template('signup.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(id=form.id.data).first()
        session_pw = form.passwd.data.encode('utf-8')
        if user and bcrypt.checkpw(session_pw, user.passwd):
            login_user(user)
            flash('Logged in successfully.', 'success')
            session['name'] = user.name
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password.')
    return render_template('login.html', form=form)


@app.route('/signout', methods=['GET'])
def signout():
    if current_user.is_authenticated:
        logout_user()
        session.pop('name', None)
        flash('You have been logged out.', 'success')
    else:
        flash("logout unsuccessful")
    return redirect(url_for('index'))


@app.route('/changepw', methods=['GET', 'POST'])
def changepw():
    form = ChangePWForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.name.data).first()
        if bcrypt.checkpw(form.challenge.data.encode('utf-8'), user.challenge):
            new_passwd = bcrypt.hashpw(
                form.new_passwd.data.encode('utf-8'), bcrypt.gensalt())
            user.passwd = new_passwd
            db.session.commit()
            flash('Password Changed')
            return redirect(url_for('login'))
        else:
            flash('Incorrect Challenge Phrase Entered')
    return render_template('changepw.html', form=form)


@app.route('/membership', methods=['GET', 'POST'])
def membership():
    return render_template('membership.html')


@app.route('/admin', methods=['GET', 'POST'])
def admin_index():
    return render_template("admin.html")


@app.route('/view_animal', methods=['GET'])
def view_animal():
    animals = Animal.query.all()
    return render_template("view_animal.html", animals=animals)


@app.route('/add_animals', methods=['GET', 'POST'])
def add_animals():
    form = AnimalForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            # Create a new animal object with form data
            new_animal = Animal(
                name=form.name.data,
                type=form.type.data,
                locations=form.locations.data,
                description=form.description.data,
                amount=form.amount.data,
                image=form.image.data
            )

            file = request.files['image']
            if file.filename == '':
                flash("Please Provide an Image")
                return render_template('add_animals.html', form=form)

            if file:
                filename = secure_filename(file.filename)
                file_path = os.path.join(
                    app.config['UPLOADED_PHOTOS_DEST'], filename)
                file.save(file_path)
                file_url = url_for('static', filename=f'uploads/{filename}')
                new_animal.image = file_url
                flash(new_animal.name)

            db.session.add(new_animal)
            db.session.commit()
            flash("Success")
            return render_template('add_animals.html', form=form,
                                   file_url=file_url)
        else:
            flash("Invalid Form Values")
            return render_template('add_animals.html', form=form)

    return render_template('add_animals.html', form=form)


@app.route('/delete_animal/<string:name>', methods=['GET', 'POST'])
def delete_animal(name):
    animal = Animal.query.filter_by(name=name).first()
    if animal:
        db.session.delete(animal)
        db.session.commit()
        flash(f"{animal.name} has been deleted")
        return redirect(url_for('view_animal'))
    else:
        flash("Animal not found")
        return redirect(url_for('view_animal'))


def membership_count():
    day_pass_count = db.session.query(
        func.count(User.id)
    ).filter(
        User.membership == 'Day pass'
    ).scalar()

    six_passes_amount_count = db.session.query(
        func.count(User.id)
    ).filter(
        User.membership == 'Six month pass'
    ).scalar()

    year_passes_amount_count = db.session.query(
        func.count(User.id)
    ).filter(
        User.membership == 'Yearly pass'
    ).scalar()

    # Print or use the count of users with each membership type
    print(f"'Day pass' membership: {day_pass_count}")
    print(
        f"'Six month pass' membership: {six_passes_amount_count}")
    print(
        f"'Yearly pass' membership: {year_passes_amount_count}")

    return day_pass_count, six_passes_amount_count, year_passes_amount_count


@app.route('/status_report', methods=['GET', 'POST'])
def status_report():

    (day_pass_count,
     six_passes_amount_count,
     year_passes_amount_count) = membership_count()

    YTDgoal = 500
    dayPassesAmount = 10 * day_pass_count
    sixPassesAmount = 30 * six_passes_amount_count
    yearPassesAmount = 50 * year_passes_amount_count
    amountRemaining = YTDgoal - (sixPassesAmount
                                 + dayPassesAmount
                                 + yearPassesAmount)

    return render_template("status_report.html",
                           amountRemaining=amountRemaining,
                           dayPassesAmount=dayPassesAmount,
                           sixPassesAmount=sixPassesAmount,
                           yearPassesAmount=yearPassesAmount)
