from flask import Flask, render_template, request
# from flask_cors import CORS
import pandas as pd 
import numpy as np
import pickle

app = Flask(__name__)
# CORS(app)
car = pd.read_csv("Cleaned Car.csv")

model = pickle.load(open("Car_price_predictor.pkl", "rb"))

@app.route("/")
def index():
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    year = sorted(car['year'].unique(),reverse = True)
    fuel_type = car['fuel_type'].unique()

    companies.insert(0,"Select Company")

    return render_template('index.html', companies = companies, car_models = car_models,years = year, fuel_type = fuel_type)

@app.route("/predict", methods=['POST'])
def predict():
    company = request.form.get('company')
    car_model = request.form.get('car_model')
    fuel = request.form.get('fuel_type')
    year = int(request.form.get('year_purchase'))
    kilo_driven = int(request.form.get('kilo_driven'))

    print(company, car_model, fuel,year, kilo_driven)

    prediction = model.predict(pd.DataFrame([[car_model, company, year, kilo_driven, fuel]], columns = ['name', 'company', 'year', 'kms_driven', 'fuel_type']))
    print(prediction)
    return str(np.round(prediction[0], 2))

if __name__ == "__main__":
    app.run(debug=True)
