'''
Project 3: Zoo Web App
Flask Initialization
Authors:
    Kyler Kramer
    Sho Vang
'''








from flask import Flask
import os
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
from flask_uploads import UploadSet, configure_uploads
from pathlib import Path
import redis
import time

app_root = Path(__file__).parent.parent

app = Flask("Authentication Web App")
app.secret_key = 'do not share'
app.config['USER SIGN UP']= 'User Sign Up"'
app.config['USER SIGNIN']= 'User Sign In"'
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(app_root, 'static', 'uploads')
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)
        count = get_hit_count()
        return 'Hit count:' .format(count)



photos = UploadSet('photos', ('png', 'jpg', 'jpeg'))
configure_uploads(app, photos)


from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db.init_app(app)

from app import models
with app.app_context(): 
    db.create_all()

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

from app.models import User


@login_manager.user_loader
def load_user(id):
    try: 
        return db.session.query(User).filter(User.id==id).one()
    except: 
        return None

from app import routes

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)