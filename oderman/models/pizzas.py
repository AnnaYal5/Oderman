from .init_db import db


class Pizzas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(15), nullable=False)
