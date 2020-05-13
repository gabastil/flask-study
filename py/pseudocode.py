from flask import Flask, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = "gabastil1.db.8756087.hostedresource.com"
# db = SQLAlchemy(app)

test_data = 'bob joe jack jane jill jess'.split()


# class User(db.Model):
#     def __repr__(self):
#         return f'<User {self.username}'


@app.route("/")
def home():
	return render_template("index.html", data=test_data, length=len(test_data))

@app.route("/<name>")
def user(name):
    data = name.split()
    return render_template("index.html", data=data, length=len(data))

@app.route("/admin/<name>")
def admin(name):
    # print(User('glenn', 'test'))
    return redirect(url_for("user", name=name))

if __name__ == "__main__":
	app.run()