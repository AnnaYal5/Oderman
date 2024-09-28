import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db(app):
    db.init_app(app)
    with app.app_context():
        if not os.path.exists('database.db'):
            db.create_all()

