from app import app, db
from app.models import User
from flask import render_template, request, redirect
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse


@app.route('/index')
@app.route('/')
@login_required
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    if current_user.is_authenticated:
        redirect('/index')
    return render_template('login.html')


@app.route('/signup')
def signup():
    if current_user.is_authenticated:
        redirect('/index')
    return render_template('signup.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect('/index')


@app.route('/loginform', methods=['GET', 'POST'])
def loginform():
    username = User.query.filter_by(username=request.form.get('username')) \
                                                            .first()
    if username is None or not username.check_password(request.form
                                                       .get('password')):
        return "Invalid Username or Password"
    login_user(username, remember=True)
    next_page = request.args.get('next')
    if not next_page or url_parse(next_page).netloc != '':
        next_page = '/index'
    return redirect(next_page)


@app.route('/signupform', methods=['GET', 'POST'])
def signupform():
    username = request.form.get('username')
    password = request.form.get('password')
    twitter_handle = request.form.get('twitter_handle')
    user = User(username=username, twitter_handle=twitter_handle)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    username = User.query.filter_by(username=request.form.get('username')) \
                                                            .first()
    if username:
        login_user(username, remember=True)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = '/index'
        return redirect(next_page)
    #  return "Registration successful"


if __name__ == '__main__':
    app.run(debug=True)
