from flask import Flask, render_template, redirect
from forms import PizzasForm
from models.pizzas import Pizzas
from models.init_db import init_db, db
import requests

app = Flask(__name__)

API_KEY = 'c1a960e0479a11c8f2487c51e0d8f51f'
BASE_URL = 'https://api.openweathermap.org/data/2.5/forecast'
CITY = 'KYIV'
DATE = '2024-10-06'
app.config['SECRET_KEY'] = 'your_secret_key'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.db'

def get_weather():
    params = {
        'q': CITY,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    print(data)


    if 'list' in data:
        for forecast in data['list']:
            forecast_date = forecast['dt_txt'].split(" ")[0]
            if forecast_date == DATE:
                return {
                    'date': forecast_date,
                    'temp': forecast['main']['temp'],
                    'description': forecast['weather'][0]['description']
                }
    else:
        print("Key 'list' not found in the response")

        return {
            'date': DATE,
            'temp': None,
            'description': 'No data available'
        }
    return None
context = get_weather()

@app.route('/')
def home():
    return render_template('index.html',**context)


@app.route('/menu')
def menu():
    pizzas = Pizzas.query.all()
    print(f"Pizzas found: {pizzas}")
    return render_template('menu.html', pizzas=pizzas, **context)


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
    return render_template('data.html', form=form, **context)




@app.route('/weather')
def index():


    return render_template('index.html',  **context)


if __name__ == '__main__':
   init_db(app=app)
   app.run(debug=True)
