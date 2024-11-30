# Car Price Prediction

This project predicts the price of a car based on various features such as brand, manufacturing year, kilometers driven, fuel type, and more. It uses machine learning models and provides a web application interface built with Flask.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [How to Run](#how-to-run)
- [Results](#results)
- [Future Improvements](#future-improvements)

---

## Project Overview

The aim of this project is to provide an easy-to-use web application that allows users to predict the price of a car by inputting its details. The project uses a machine learning model trained on a dataset of used car listings and integrates it with a Flask-based web application for deployment.

---

## Dataset

The dataset, `car_data.csv`, contains the following columns:

- `name`: The name of the car.
- `company`: The manufacturer of the car.
- `year`: The year of manufacture.
- `Price`: The selling price of the car.
- `kms_driven`: The distance the car has been driven in kilometers.
- `fuel_type`: The type of fuel used by the car.

### Cleaning and Preprocessing

- Removed duplicates and invalid entries.
- Converted non-numeric columns like `kms_driven` to numeric.
- Encoded categorical features like `company` and `fuel_type`.

---

## Features

- Predicts car prices based on:
  - Brand
  - Manufacturing year
  - Kilometers driven
  - Fuel type
- Provides a user-friendly web application interface.

---

## Technologies Used

- **Python**: Core programming language.
- **Flask**: For building the web application.
- **Machine Learning**:
  - Linear Regression
  - Ridge Regression
- **Libraries**: 
  - `pandas` for data manipulation.
  - `numpy` for numerical computations.
  - `matplotlib` and `seaborn` for data visualization.
  - `scikit-learn` for building and evaluating the machine learning models.
  - `pickle` for model serialization.

---

## Setup and Installation

### Prerequisites

- Python 3.7 or higher
- Required libraries listed in `requirements.txt`.

### Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/car-price-prediction.git
   cd car-price-prediction
2. Install dependencies:
    ```bash
    pip install -r requirements.txt

3. Ensure the dataset car_data.csv is in the project directory.

4. Run the notebook:
    ```bash
    jupyter notebook Predictor.ipynb