from flask import Flask, render_template,request,redirect
from data import Pizzas


app = Flask(__name__)

test_name = "Discount base"
discount = "4"
customers = [
    {'name': "Anna", 'order': "5"},
    {'name': "Dany", 'order': "7"},
    {'name': "Rita", 'order': "1"},
    {'name': "Taya", 'order': "6"},
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/menu')
def menu():
    pizzas = Pizzas.query.all()
    context = {
        "customers": customers,
        "test_name": test_name,
        "discount": discount
    }
    return render_template('menu.html', **context, pizzas=pizzas)


@app.route('/add_item', methods=["POST"])
def add_item():
    name = request.form['name']
    description = request.form['description']
    price = request.form['price']
    category = request.form['category']
    insert_into_table(name, description, price, category)
    return redirect('/menu')

@app.route('/add')
def add_form():
    return render_template('data.html')

