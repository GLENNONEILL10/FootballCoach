from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(50),unique=True, nullable=False)
    password = db.Column(db.String(200),nullable=False)

    submissions = db.relationship('Submission', backref='user', lazy=True)


class Submission(db.Model):
    __tablename__ = 'submissions'
    submission_id = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.String(50), nullable=False)
    inputted_data = db.Column(db.Text, nullable=False)
    calculated_data = db.Column(db.Text, nullable=False)
    timeStamp = db.Column(db.DateTime(timezone=True), default=datetime.now)

    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
