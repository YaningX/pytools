from flasky import app



@app.route("/")
@app.route("/index")
def index():
    return "hello onion"