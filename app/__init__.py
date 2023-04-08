

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flask_migrate import Migrate
from flask_cors import CORS
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
# CORS(app, origins=['http://127.0.0.1:5173'])
csrf = CSRFProtect(app)
app.config.from_object(Config)

db = SQLAlchemy(app)

migrate = Migrate(app, db)

from app import models
from app import views

with app.app_context():
    db.create_all()
