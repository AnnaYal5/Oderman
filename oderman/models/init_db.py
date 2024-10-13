import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db(app):
    db.init_app(app)
    with app.app_context():
        if not os.path.exists('database.db'):
            db.create_all()

class Survey(db.Model):
    __tablename__ = 'survey'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(250), nullable=False)


class Answer(db.Model):
    __tablename__ = 'answer'
    id = db.Column(db.Integer, primary_key=True)
    survey_id = db.Column(db.Integer, db.ForeignKey('survey.id'))
    answer = db.Column(db.String(250), nullable=False)
    survey = db.relationship('Survey', backref=db.backref('answers', lazy=True))
