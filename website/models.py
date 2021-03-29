from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Flip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    highest_streak = db.Column(db.Integer)
    wins = db.Column(db.Integer)
    loses = db.Column(db.Integer)
    total_games = db.Column(db.Integer)
    win_percentage = db.Column(db.Integer)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    flips = db.relationship('Flip')