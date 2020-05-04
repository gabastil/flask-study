from flask import Flask, url_for, redirect, render_template

app = Flask(__name__)

test_data = 'bob joe jack jane jill jess'.split()

@app.route("/")
def home():
	return render_template("index.html", data=test_data, length=len(test_data))

@app.route("/<name>")
def user(name):
    data = name.split()
    return render_template("index.html", data=data, length=len(data))

@app.route("/admin/<name>")
def admin(name):
    return redirect(url_for("user", name=name))

if __name__ == "__main__":
	app.run()