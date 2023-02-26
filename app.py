from flask import Flask

app = Flask(__name__)

@app.route("/ghar-phoenix")
def home() -> str:
    print("Inside ghar-phoenix.")
    print("Will write more logic later on.")
    return "Hello from Vinay inside home Function v.0.0.1!"

@app.route("/store")
def shop() -> str:
    print("Inside shop")
    print("Will write more logic later on.")
    return "Hello from Vinay inside shop Function v.0.0.2!"