# 🏠 Indore Student Rental Fair-Price Estimator

## 📌 Project Overview

The Indore Student Rental Fair-Price Estimator is a machine learning-based application designed to help students evaluate whether a room or flat rental price in Indore is reasonable.

The system estimates the fair monthly rent based on property characteristics such as location, area, BHK, sharing type, furnishing, parking, WiFi, food availability, bathroom facilities, distance from college and security deposit.

It then compares the predicted fair rent with the listed rent and classifies the property as:

- 🟢 GOOD DEAL
- 🟡 FAIR PRICE
- 🔴 OVERPRICED

## 🎯 Objectives

- Estimate fair rent for student-friendly rooms and flats.
- Identify overpriced rental listings.
- Help students make better rental decisions.
- Apply machine learning regression techniques to rental-price estimation.
- Develop a simple web-based rental analysis application.

## 📊 Dataset

The project uses a student rental dataset containing property and rental characteristics for Indore.

Important variables include:

- Location
- Property Type
- Area (sq.ft.)
- BHK
- Sharing Type
- Bathrooms
- Furnishing
- Parking
- WiFi
- Food
- Attached Bathroom
- Distance from College
- Security Deposit
- Monthly Rent

## 🤖 Machine Learning Models

Two regression models were evaluated:

1. Linear Regression
2. Random Forest Regression

### Model Evaluation

| Model | MAE | RMSE | R² Score |
|---|---:|---:|---:|
| Linear Regression | ₹863 | ₹1,205 | 0.9085 |
| Random Forest | ₹798.57 | ₹1,210.11 | 0.9077 |

Random Forest was selected as the final model based on its lower Mean Absolute Error.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- GitHub

## ⚙️ Application Workflow

```text
Rental Property Details
        ↓
Data Preprocessing
        ↓
Machine Learning Model
        ↓
Fair Rent Prediction
        ↓
Compare with Listed Rent
        ↓
Good Deal / Fair Price / Overpriced
