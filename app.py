import streamlit as st
import pandas as pd
import joblib
import os
import glob

# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "student_rent_model.pkl"
)

model = joblib.load(MODEL_PATH)

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Indore Student Rent Estimator",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 Indore Student Rental Fair-Price Estimator")

st.write(
    "Estimate fair monthly rent for student rooms and flats in Indore."
)

st.divider()

# --------------------------------------------------
# USER INPUTS
# --------------------------------------------------

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
    [
        "PG",
        "Single Room",
        "Shared Room",
        "1 BHK",
        "2 BHK"
    ]
)

area_sqft = st.number_input(
    "Area (sq.ft.)",
    min_value=50,
    max_value=3000,
    value=600
)

bhk = st.selectbox(
    "BHK",
    [0, 1, 2]
)

sharing = st.selectbox(
    "Sharing",
    [
        "Single",
        "Double",
        "Triple",
        "Whole Property"
    ]
)

bathrooms = st.selectbox(
    "Bathrooms",
    [1, 2, 3]
)

attached_bathroom = st.selectbox(
    "Attached Bathroom",
    ["Yes", "No"]
)

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

# --------------------------------------------------
# ESTIMATE FAIR RENT
# --------------------------------------------------

if st.button(
    "🔍 Estimate Fair Rent",
    use_container_width=True
):

    # These fields are kept internally because
    # the existing trained model expects them.
    # They are NOT shown to the user.

    furnishing = "Semi-Furnished"
    parking = "No"
    wifi = "Yes"
    food = "No"

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

    # Prediction
    fair_rent = model.predict(input_data)[0]
    fair_rent = round(fair_rent)

    # Difference
    difference_percent = (
        (listed_rent - fair_rent) / fair_rent
    ) * 100

    # --------------------------------------------------
    # RENTAL ANALYSIS
    # --------------------------------------------------

    st.subheader("📊 Rental Analysis")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Listed Rent",
            f"₹{listed_rent:,}"
        )

    with col2:
        st.metric(
            "Estimated Fair Rent",
            f"₹{fair_rent:,}"
        )

    st.write(
        f"Difference from fair rent: "
        f"**{difference_percent:.2f}%**"
    )

    if difference_percent > 10:

        st.error("🔴 OVERPRICED")

        st.write(
            "This property is significantly above "
            "the estimated fair rent."
        )

    elif difference_percent < -10:

        st.success("🟢 GOOD DEAL")

        st.write(
            "This property is below the estimated fair rent."
        )

    else:

        st.info("🟡 FAIR PRICE")

        st.write(
            "The listed rent is close to the estimated fair rent."
        )

    # --------------------------------------------------
    # OTHER ROOM SUGGESTIONS
    # --------------------------------------------------

    st.divider()

    st.subheader("🏘️ Other Room Suggestions")

    st.write(
        "Here are some alternative properties that "
        "may also suit your requirements:"
    )

    # Find CSV file automatically
    csv_files = glob.glob(
        os.path.join(BASE_DIR, "*.csv")
    )

    data_file = None

    for file in csv_files:

        filename = os.path.basename(file).lower()

        if "rental" in filename or "rent" in filename:
            data_file = file
            break

    if data_file is None and len(csv_files) > 0:
        data_file = csv_files[0]

    if data_file is not None:

        try:

            df = pd.read_csv(data_file)

            # Required columns
            required_columns = [
                "location",
                "property_type",
                "area_sqft",
                "bhk",
                "sharing",
                "bathrooms",
                "rent"
            ]

            available_columns = [
                col for col in required_columns
                if col in df.columns
            ]

            if "rent" not in df.columns:

                st.warning(
                    "Rental price column was not found in the dataset."
                )

            else:

                suggestions = df.copy()

                # Remove current exact listing if listing_id exists
                if "listing_id" in suggestions.columns:
                    suggestions = suggestions[
                        suggestions["listing_id"].notna()
                    ]

                # Convert rent to numeric
                suggestions["rent"] = pd.to_numeric(
                    suggestions["rent"],
                    errors="coerce"
                )

                suggestions = suggestions.dropna(
                    subset=["rent"]
                )

                # --------------------------------------------------
                # Prefer similar properties
                # --------------------------------------------------

                similar = suggestions[
                    (
                        suggestions["location"] == location
                    )
                    &
                    (
                        suggestions["property_type"]
                        == property_type
                    )
                ].copy()

                # If not enough results, use property type
                if len(similar) < 3:

                    similar = suggestions[
                        suggestions["property_type"]
                        == property_type
                    ].copy()

                # If still not enough, use all properties
                if len(similar) < 3:

                    similar = suggestions.copy()

                # --------------------------------------------------
                # Calculate closeness to estimated fair rent
                # --------------------------------------------------

                similar["rent_difference"] = (
                    similar["rent"] - fair_rent
                ).abs()

                similar = similar.sort_values(
                    "rent_difference"
                )

                # Top 5 suggestions
                similar = similar.head(5)

                # --------------------------------------------------
                # Display suggestions
                # --------------------------------------------------

                for i, (_, row) in enumerate(
                    similar.iterrows(),
                    start=1
                ):

                    st.markdown(
                        f"### 🏠 Option {i}"
                    )

                    col1, col2 = st.columns(2)

                    with col1:

                        if "location" in row:
                            st.write(
                                f"📍 **Location:** "
                                f"{row['location']}"
                            )

                        if "property_type" in row:
                            st.write(
                                f"🏢 **Property:** "
                                f"{row['property_type']}"
                            )

                        if "area_sqft" in row:
                            st.write(
                                f"📐 **Area:** "
                                f"{row['area_sqft']} sq.ft."
                            )

                    with col2:

                        if "bhk" in row:
                            st.write(
                                f"🛏️ **BHK:** "
                                f"{row['bhk']}"
                            )

                        if "sharing" in row:
                            st.write(
                                f"👥 **Sharing:** "
                                f"{row['sharing']}"
                            )

                        st.write(
                            f"💰 **Monthly Rent:** "
                            f"₹{int(row['rent']):,}"
                        )

                    st.divider()

        except Exception as e:

            st.warning(
                "Alternative room suggestions "
                "could not be loaded."
            )

    else:

        st.info(
            "Add the rental CSV dataset to the GitHub repository "
            "to display alternative room suggestions."
        )
        
