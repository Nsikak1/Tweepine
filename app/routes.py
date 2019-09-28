from app import app
from flask import render_template


@app.route('/index')
def hello():
    return "hello"


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/login')
def login():
    return render_template("login.html")
