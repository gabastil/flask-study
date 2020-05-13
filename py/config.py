import os

class Config():
    SECRET_KEY = os.environ.get("SECRET_KEY") or "3DMOTwanRUup3eNqN"
    SQLALCHEMY_DATABASE_URI = "flaskstudy.mysql.pythonanywhere-services.com"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
