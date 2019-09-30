from app import db, login
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    twitter_handle = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    tweets = db.relationship('Tweets', backref='author', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Tweets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tweet = db.Column(db.String(1000))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Tweets: {}>'.format(self.tweet)
