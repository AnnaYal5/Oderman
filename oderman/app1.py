from flask import Flask, render_template, redirect, jsonify, request
from forms import PizzasForm
from models.pizzas import Pizzas
from models.init_db import init_db, db,Survey,Answer
import requests
from sqlalchemy.orm import validates


app = Flask(__name__)

API_KEY = 'c1a960e0479a11c8f2487c51e0d8f51f'
BASE_URL = 'https://api.openweathermap.org/data/2.5/forecast'
CITY = 'KYIV'
DATE = '2024-10-06'
app.config['SECRET_KEY'] = 'your_secret_key'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.db'

db.init_app(app=app)

with app.app_context():
    db.create_all()


@validates('answer')
def validate_answer(self, key, value: str):
    if value.strip() == '':
        raise ValueError('can not be an empty string')
    return value


with app.app_context():
     if Survey.query.count() == 0:
        new_survey = Survey(question='Щоб хотіли бачити у меню??')
        db.session.add(new_survey)
        db.session.commit()
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
        print(f"Error occurred: {e}")

# with app.app_context():
#     db.session.query(Survey).delete()
#     db.session.commit()
def get_weather():
    params = {
        'q': CITY,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

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


@app.route('/survey/<int:survey_id>')
def survey(survey_id):
    survey = Survey.query.get_or_404(survey_id)
    answers = survey.answers
    return render_template('survey.html', survey=survey, answers=answers)



@app.route('/submit', methods=["POST"])
def submit():
    answer = request.form.get('answer')
    survey_id = request.form.get('survey_id')
    answer_model = Answer(survey_id=survey_id, answer=answer)
    db.session.add(answer_model)
    db.session.commit()
    return jsonify({'status': "success"})


@app.route('/heder')
def header():
    return render_template('header.html',**context)
@app.route('/')
def home():
    surveys = Survey.query.all()
    return render_template('index.html', surveys=surveys)


@app.route('/menu')
def menu():
    pizzas = Pizzas.query.all()
    print(f"Pizzas found: {pizzas}")
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

   app.run(debug=True)
