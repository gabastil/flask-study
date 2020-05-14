import os

class Config():
    SECRET_KEY = os.environ.get("SECRET_KEY") or "---!"

    __ROOT = f'mysql://gabastil1:{SECRET_KEY}'
    __DB = '@gabastil1.db.8756087.hostedresource.com/gabastil1'

    SQLALCHEMY_DATABASE_URI = __ROOT + __DB

    SQLALCHEMY_TRACK_MODIFICATIONS = True
