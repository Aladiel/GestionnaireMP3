from flask import render_template, Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def index():
    print("Hello World")
    return render_template("index.html")