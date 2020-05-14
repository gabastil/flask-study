from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .forms import LoginForm
from .config import Config
from .models import User, Post
from . import routes, models

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
