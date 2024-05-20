'''
Project 3: Zoo Web App
Flask-WTF Forms
Authors:
    Kyler Kramer
    Sho Vang
'''




from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired
from wtforms import FileField, SelectField
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class SignUpForm(FlaskForm):
    id = StringField('Username', validators=[DataRequired()])
    phoneNumber = StringField('Phone Number')
    name = StringField('Name', validators=[DataRequired()])
    passwd = PasswordField('Password', validators=[DataRequired()])
    membership = SelectField('Membership Status', choices=[
        ('Free', 'Free'),
        ('Day pass', 'Day pass'),
        ('Six month pass', 'Six month pass'),
        ('Yearly pass', 'Yearly pass')
    ], validators=[DataRequired()])
    passwd_confirm = PasswordField(
        'Confirm Password', validators=[DataRequired()])
    challenge = StringField('Challenge Phrase', validators=[DataRequired()])
    submit = SubmitField('Confirm')


class LoginForm(FlaskForm):
    id = StringField('Username', validators=[DataRequired()])
    passwd = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Confirm')
    changepw = SubmitField('Change Password')


class ChangePWForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    challenge = StringField('Challenge Phrase', validators=[DataRequired()])
    new_passwd = PasswordField('New Password', validators=[DataRequired()])


class AnimalForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    type = StringField('Type', validators=[DataRequired()])
    locations = StringField('Locations', validators=[DataRequired()])
    description = StringField('Description')
    amount = IntegerField('Amount', validators=[DataRequired()])
    image = FileField('Image')
    submit = SubmitField('Submit')
