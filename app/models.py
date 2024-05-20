'''
Project 3: Zoo Web App
SQLite Models
Authors:
    Kyler Kramer
    Sho Vang
'''






from app import db
from flask_login import UserMixin
from wtforms import SelectField
from wtforms.validators import DataRequired


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column('ID', db.String, primary_key=True)
    name = db.Column('Name', db.String)
    phoneNumber = db.Column('Phone_Number', db.String(20))
    passwd = db.Column('Password', db.LargeBinary)
    membership = db.Column('Membership', db.String)
    challenge = db.Column('Challenge_Phrase', db.LargeBinary)
    admin = db.Column(db.Boolean, default=False)


class Animal(db.Model):
    __tablename__ = 'animals'
    name = db.Column("Name", db.String, primary_key=True)
    type = db.Column("Type", db.String)
    locations = db.Column("Locations", db.String)
    description = db.Column("Description", db.String)
    amount = db.Column("Amount", db.String)
    image = db.Column("Image", db.String, default='N/A')


class status_report ():
    YTDgoal = 500
    dayPassesAmount = 10
    sixPassesAmount = 30
    yearPassesAmount = 50
    amountRemaining = YTDgoal - (dayPassesAmount
                                 + sixPassesAmount
                                 + yearPassesAmount)
