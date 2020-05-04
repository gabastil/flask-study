from app import app

@app.route("/")
@app.route("/index")
def index(message='Hello World'):
	return message
