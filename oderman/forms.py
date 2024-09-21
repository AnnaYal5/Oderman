from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class PizzasForm(FlaskForm):
    name = StringField(label="Name", validators=[DataRequired()])
    price = StringField(label="Price")
    category = StringField(label="Category")
    submit = SubmitField('Додати піцу')
