from flask import url_for, redirect, render_template, flash
from app import app, LoginForm

route = app.route

names = 'Bob Joe Jack Jane Jill Jess'.split()
kwargs = {'data': names, 'length': len(names)}


@route("/home")
@route("/")
def home():
    return render_template("index.html", **kwargs)


@route("/<name>")
def user(name):
    kwargs = {'data': [name], 'length': 1}
    return render_template("index.html", **kwargs)


@route("/admin/<name>")
def admin(name):
    return redirect(url_for("user", name=name))


@route("/signin", methods=['GET', 'POST'])
def signin():
    form = LoginForm()
    # flash("Hello")
    if form.validate_on_submit():
        message = f"Login required for {form.username.data}. " +\
                  f"Remember me {form.remember_me.data}"
        flash(message)
        return redirect(url_for("home"))
    return render_template("signin.html", form=form)
