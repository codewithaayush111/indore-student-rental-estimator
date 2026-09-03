import streamlit as st
import pandas as pd
import joblib
import os
import glob
import streamlit.components.v1 as components
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
    layout="wide"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------


# ---------- ANIMATED HERO ----------

components.html("""
<!DOCTYPE html>
<html>
<head>
<style>

body {
    margin: 0;
    overflow: hidden;
    font-family: Arial, sans-serif;
}

.hero {
    height: 300px;
    border-radius: 24px;
    background: linear-gradient(135deg, #eaf6ff, #f5edff);
    position: relative;
    overflow: hidden;
    box-shadow: 0 12px 35px rgba(0,0,0,0.12);
}

/* Main title */
.title {
    position: absolute;
    top: 28px;
    width: 100%;
    text-align: center;
    font-size: 30px;
    font-weight: bold;
    color: #20242a;
}

/* Student */
.student {
    position: absolute;
    left: 18%;
    bottom: 55px;
    font-size: 65px;
    animation: walk 4s ease-in-out infinite;
}

/* House */
.house {
    position: absolute;
    right: 18%;
    bottom: 48px;
    font-size: 90px;
    animation: float 3s ease-in-out infinite;
}

/* Rent card */
.card {
    position: absolute;
    top: 85px;
    left: 50%;
    transform: translateX(-50%);
    background: white;
    padding: 13px 25px;
    border-radius: 16px;
    text-align: center;
    box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    animation: cardFloat 2.5s ease-in-out infinite;
}

.card-title {
    font-size: 15px;
    color: #666;
}

.price {
    font-size: 25px;
    font-weight: bold;
    color: #222;
}

/* Walking animation */
@keyframes walk {
    0% {
        transform: translateX(-20px);
    }

    50% {
        transform: translateX(120px);
    }

    100% {
        transform: translateX(-20px);
    }
}

/* House floating */
@keyframes float {
    0%, 100% {
        transform: translateY(0);
    }

    50% {
        transform: translateY(-8px);
    }
}

/* Card floating */
@keyframes cardFloat {
    0%, 100% {
        transform: translateX(-50%) translateY(0);
    }

    50% {
        transform: translateX(-50%) translateY(-8px);
    }
}

</style>
</head>

<body>

<div class="hero">

    <div class="title">
        🏠 Find Your Perfect Student Rental
    </div>

    <div class="student">
        🧑‍🎓
    </div>

    <div class="card">
        <div class="card-title">💰 Estimated Fair Rent</div>
        <div class="price">₹12,500 / month</div>
    </div>

    <div class="house">
        🏠
    </div>

</div>

</body>
</html>
""", height=320)

# HEADER
# --------------------------------------------------

st.markdown(
    '<div class="main-title">🏠 Indore Student Rental Fair-Price Estimator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Find a fair rental price and discover alternative student-friendly properties in Indore.'
    '</div>',
    unsafe_allow_html=True
)

st.divider()

# --------------------------------------------------
# INPUT SECTION
# --------------------------------------------------

st.markdown(
    '<div class="section-title">📋 Property Details</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:

    location = st.selectbox(
        "📍 Location",
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
        "🏢 Property Type",
        [
            "PG",
            "Single Room",
            "Shared Room",
            "1 BHK",
            "2 BHK"
        ]
    )

    area_sqft = st.number_input(
        "📐 Area (sq.ft.)",
        min_value=50,
        max_value=3000,
        value=600
    )

with col2:

    bhk = st.selectbox(
        "🛏️ BHK",
        [0, 1, 2]
    )

    sharing = st.selectbox(
        "👥 Sharing",
        [
            "Single",
            "Double",
            "Triple",
            "Whole Property"
        ]
    )

    bathrooms = st.selectbox(
        "🚿 Bathrooms",
        [1, 2, 3]
    )

with col3:

    attached_bathroom = st.selectbox(
        "🚿 Attached Bathroom",
        ["Yes", "No"]
    )

    distance_from_college_km = st.number_input(
        "🎓 Distance from College (km)",
        min_value=0.1,
        max_value=20.0,
        value=1.5
    )

    security_deposit = st.number_input(
        "💰 Security Deposit (₹)",
        min_value=0,
        max_value=100000,
        value=15000
    )

listed_rent = st.number_input(
    "🏷️ Listed Monthly Rent (₹)",
    min_value=1000,
    max_value=100000,
    value=12000
)

st.divider()

# --------------------------------------------------
# ESTIMATE BUTTON
# --------------------------------------------------

if st.button(
    "🔍  Estimate Fair Rent",
    use_container_width=True,
    type="primary"
):

    # Existing model still expects these fields.
    # They are kept internally and are not shown to the user.

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

    # --------------------------------------------------
    # MODEL PREDICTION
    # --------------------------------------------------

    fair_rent = model.predict(input_data)[0]
    fair_rent = round(fair_rent)

    difference_percent = (
        (listed_rent - fair_rent) / fair_rent
    ) * 100

    # --------------------------------------------------
    # RENTAL ANALYSIS
    # --------------------------------------------------

    st.markdown(
        '<div class="section-title">📊 Rental Analysis</div>',
        unsafe_allow_html=True
    )

    result1, result2, result3 = st.columns(3)

    with result1:
        st.metric(
            "🏷️ Listed Rent",
            f"₹{listed_rent:,}"
        )

    with result2:
        st.metric(
            "💰 Estimated Fair Rent",
            f"₹{fair_rent:,}"
        )

    with result3:
        st.metric(
            "📈 Difference",
            f"{difference_percent:.2f}%"
        )

    # --------------------------------------------------
    # PRICE STATUS
    # --------------------------------------------------

    if difference_percent > 10:

        st.error(
            "🔴 OVERPRICED — This property is significantly "
            "above the estimated fair rent."
        )

    elif difference_percent < -10:

        st.success(
            "🟢 GOOD DEAL — This property is below "
            "the estimated fair rent."
        )

    else:

        st.info(
            "🟡 FAIR PRICE — The listed rent is close "
            "to the estimated fair rent."
        )

    # --------------------------------------------------
    # OTHER ROOM SUGGESTIONS
    # --------------------------------------------------

    st.divider()

    st.markdown(
        '<div class="section-title">🏘️ Other Room Suggestions</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Based on your selected property type and location, "
        "here are some alternative options you may consider:"
    )

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

            if "rent" not in df.columns:

                st.warning(
                    "Rental price column was not found in the dataset."
                )

            else:

                suggestions = df.copy()

                suggestions["rent"] = pd.to_numeric(
                    suggestions["rent"],
                    errors="coerce"
                )

                suggestions = suggestions.dropna(
                    subset=["rent"]
                )

                # Prefer same location + property type
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

                # If fewer than 3, use same property type
                if len(similar) < 3:

                    similar = suggestions[
                        suggestions["property_type"]
                        == property_type
                    ].copy()

                # If still fewer than 3, use complete dataset
                if len(similar) < 3:

                    similar = suggestions.copy()

                # Find closest rent to predicted fair rent
                similar["rent_difference"] = (
                    similar["rent"] - fair_rent
                ).abs()

                similar = similar.sort_values(
                    "rent_difference"
                )

                similar = similar.head(5)

                # --------------------------------------------------
                # DISPLAY CARDS
                # --------------------------------------------------

                for i, (_, row) in enumerate(
                    similar.iterrows(),
                    start=1
                ):

                    st.markdown(
                        f'<div class="suggestion-box">'
                        f'<h3>🏠 Option {i}</h3>',
                        unsafe_allow_html=True
                    )

                    s1, s2, s3 = st.columns(3)

                    with s1:

                        if "location" in row:
                            st.write(
                                f"📍 **Location:** {row['location']}"
                            )

                        if "property_type" in row:
                            st.write(
                                f"🏢 **Property:** "
                                f"{row['property_type']}"
                            )

                    with s2:

                        if "area_sqft" in row:
                            st.write(
                                f"📐 **Area:** "
                                f"{row['area_sqft']} sq.ft."
                            )

                        if "bhk" in row:
                            st.write(
                                f"🛏️ **BHK:** {row['bhk']}"
                            )

                    with s3:

                        if "sharing" in row:
                            st.write(
                                f"👥 **Sharing:** "
                                f"{row['sharing']}"
                            )

                        st.write(
                            f"💰 **Monthly Rent:** "
                            f"₹{int(row['rent']):,}"
                        )

                    st.markdown(
                        '</div>',
                        unsafe_allow_html=True
                    )

        except Exception:

            st.warning(
                "Alternative room suggestions could not be loaded."
            )

    else:

        st.info(
            "Rental dataset not found in the repository."
        )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.markdown(
    '<div class="small-text" style="text-align:center;">'
    '📍 Designed for student rental analysis in Indore '
    '| Machine Learning based estimation'
    '</div>',
    unsafe_allow_html=True
)
