from app import app
from app.models import User
from flask import render_template, request, redirect
from flask_login import current_user, login_user


@app.route('/index')
def hello():
    return "hello"


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/login')
def login():
    if current_user.is_authenticated:
        redirect('/index')
    return render_template("login.html")


@app.route('/form', methods=['GET', 'POST'])
def form():
    username = User.query.filter_by(username=request.form.get('username')).first()
    if username is None or not username.check_password(request.form.get('password')):
        return "Invalid Username or Password"
    login_user(username, remember=True)
    return "Welcome {}".format(username.username)


if __name__ == '__main__':
    app.run(debug=True)
