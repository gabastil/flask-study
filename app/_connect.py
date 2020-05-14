from models import User, Post
from . import db

u = User(username='glenn', email='test@test.com')
db.session.add(u)