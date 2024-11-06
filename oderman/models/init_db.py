import os
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,TextAreaField
from wtforms.validators import DataRequired

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

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    reviews = db.Column(db.String(100), nullable=False, unique=True)

class ReviewsForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    reviews = TextAreaField('Reviews', validators=[DataRequired()])
    submit = SubmitField('Submit')
