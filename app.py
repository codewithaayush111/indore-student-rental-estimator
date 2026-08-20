
import streamlit as st
import pandas as pd
import joblib

# Load model
import os
import joblib

MODEL_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "student_rent_model.pkl"
)

model = joblib.load(MODEL_PATH)

st.set_page_config(
    page_title="Indore Student Rent Estimator",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 Indore Student Rental Fair-Price Estimator")
st.write("Estimate fair monthly rent for student rooms and flats in Indore.")

st.divider()

location = st.selectbox(
    "Location",
    [
        "Vijay Nagar",
        "Bhawarkua",
        "Rau",
        "Palasia",
        "Bengali Square",
        "Geeta Bhawan",
        "Sukhliya",
        "Scheme 54",
        "LIG Colony",
        "Bicholi Mardana"
    ]
)

property_type = st.selectbox(
    "Property Type",
    ["PG", "Single Room", "Shared Room", "1 BHK", "2 BHK"]
)

area_sqft = st.number_input(
    "Area (sq.ft.)",
    min_value=50,
    max_value=3000,
    value=600
)

bhk = st.selectbox("BHK", [0, 1, 2])

sharing = st.selectbox(
    "Sharing",
    ["Single", "Double", "Triple", "Whole Property"]
)

bathrooms = st.selectbox("Bathrooms", [1, 2, 3])

furnishing = st.selectbox(
    "Furnishing",
    ["Fully Furnished", "Semi-Furnished", "Unfurnished"]
)

parking = st.selectbox("Parking", ["Yes", "No"])
wifi = st.selectbox("WiFi", ["Yes", "No"])
food = st.selectbox("Food Included", ["Yes", "No"])
attached_bathroom = st.selectbox("Attached Bathroom", ["Yes", "No"])

distance_from_college_km = st.number_input(
    "Distance from College (km)",
    min_value=0.1,
    max_value=20.0,
    value=1.5
)

security_deposit = st.number_input(
    "Security Deposit (₹)",
    min_value=0,
    max_value=100000,
    value=15000
)

listed_rent = st.number_input(
    "Listed Monthly Rent (₹)",
    min_value=1000,
    max_value=100000,
    value=12000
)

st.divider()

if st.button("🔍 Estimate Fair Rent", use_container_width=True):

    input_data = pd.DataFrame([{
        "location": location,
        "property_type": property_type,
        "area_sqft": area_sqft,
        "bhk": bhk,
        "sharing": sharing,
        "bathrooms": bathrooms,
        "furnishing": furnishing,
        "parking": parking,
        "wifi": wifi,
        "food": food,
        "attached_bathroom": attached_bathroom,
        "distance_from_college_km": distance_from_college_km,
        "security_deposit": security_deposit
    }])

    fair_rent = model.predict(input_data)[0]
    fair_rent = round(fair_rent)

    difference_percent = (
        (listed_rent - fair_rent) / fair_rent
    ) * 100

    st.subheader("📊 Rental Analysis")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Listed Rent", f"₹{listed_rent:,}")

    with col2:
        st.metric("Estimated Fair Rent", f"₹{fair_rent:,}")

    st.write(
        f"Difference from fair rent: **{difference_percent:.2f}%**"
    )

    if difference_percent > 10:
        st.error("🔴 OVERPRICED")
        st.write("This property is significantly above the estimated fair rent.")

    elif difference_percent < -10:
        st.success("🟢 GOOD DEAL")
        st.write("This property is below the estimated fair rent.")

    else:
        st.info("🟡 FAIR PRICE")
        st.write("The listed rent is close to the estimated fair rent.")
