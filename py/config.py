import os

class Config():
    SECRET_KEY = os.environ.get("MYSQL") or ""

    _ROOT = f'mysql://gabastil1:{SECRET_KEY}'
    _DB = '@gabastil1.db.8756087.hostedresource.com/gabastil1'

    SQLALCHEMY_DATABASE_URI = _ROOT + _DB
    SQLALCHEMY_TRACK_MODIFICATIONS = False
