from app import app
from flask import render_template, request


@app.route('/index')
def hello():
    return "hello"


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/form', methods=['GET', 'POST'])
def form():
    username = request.form.get('username')
    password = request.form.get('password')
    return "Your Username is: {} and the Password is: {}".format(username, password)


if __name__ == '__main__':
    app.run(debug=True)
