from flask import Flask, render_template, redirect
from forms import PizzasForm
from models.pizzas import Pizzas
from models.init_db import init_db, db


app = Flask(__name__)


app.config['SECRET_KEY'] = 'your_secret_key'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.db'


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
        print('YES!')
        new_pizza = Pizzas(
            name=form.name.data,
            price=form.price.data,
            category=form.category.data
        )
        db.session.add(new_pizza)
        db.session.commit()
        return redirect('/')
    return render_template('data.html', form=form)


if __name__ == '__main__':
   init_db(app=app)
   app.run(debug=True)