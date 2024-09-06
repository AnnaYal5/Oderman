from flask import Flask, render_template
import sqlite3
app = Flask(__name__)

pizzas = [
    {'name': "Маргарита", "ingredients": "соус , сир, базилік", "price": "150 грн"},
    {'name': "Папероні", "ingredients": "соус , сир, папероні", "price": "190 грн"},
    {'name': "Гавайська", "ingredients": "соус , сир, ананас, шинка", "price": "200 грн"}
]
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
    context = {
        "customers": customers,
        "test_name": test_name,
        "discount": discount
    }
    return render_template('menu.html', pizzas=pizzas, **context)


@app.route('/add')
def add_form():
    return render_template('data.html')


if __name__ == '__main__':
    app.run(debug=True)