from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("../index.html", data='this is a test'.split())

if __name__ == "__main__":
	app.run()