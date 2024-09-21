from flask import Flask, render_template, request, redirect
from forms import PizzasForm
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SECRET_KEY'] = 'your_secret_key'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.db'


db = SQLAlchemy(app)

class Pizzas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(15), nullable=False)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/menu')
def menu():
    pizzas = Pizzas.query.all()
    print(f"Pizzas found: {pizzas}")  # Check if pizzas are retrieved
    return render_template('menu.html', pizzas=pizzas)

@app.route('/add_item', methods=["GET", "POST"])
def add_pizzas():
    form = PizzasForm()
    if form.validate_on_submit():
        new_pizza = Pizzas(
            name=form.name.data,
            price=form.price.data,
            category=form.category.data
        )
        db.session.add(new_pizza)
        db.session.commit()
        return redirect('/')
    return render_template('data.html', form=form)

from sqlalchemy import inspect

@app.before_request
def create_tables():
    # Створюємо інспектор для перевірки наявності таблиць
    inspector = inspect(db.engine)
    # Перевіряємо, чи існує таблиця 'pizzas'
    if not inspector.has_table('pizzas'):
        db.create_all()

if __name__ == '__main__':
    app.run(debug=True)