# app.py

from flask import Flask
from flask_login import LoginManager
from models.users import db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Password123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'