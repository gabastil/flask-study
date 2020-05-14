from flask import Flask, url_for, redirect, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from . import Config
from . import LoginForm

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)


route = app.route





if __name__ == "__main__":
    app.run()
