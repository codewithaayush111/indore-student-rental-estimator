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
# ---------- PREMIUM ANIMATED HERO ----------

components.html("""
<!DOCTYPE html>
<html>
<head>

<style>

* {
    box-sizing: border-box;
}

body {
    margin: 0;
    overflow: hidden;
    font-family: Arial, sans-serif;
}

.hero {
    height: 380px;
    width: 100%;
    border-radius: 28px;
    position: relative;
    overflow: hidden;

    background:
        radial-gradient(circle at 85% 20%, rgba(120,180,255,0.35), transparent 30%),
        radial-gradient(circle at 15% 85%, rgba(180,120,255,0.25), transparent 30%),
        linear-gradient(135deg, #eef7ff, #f6efff);

    box-shadow:
        0 25px 60px rgba(0,0,0,0.14);

    border: 1px solid rgba(255,255,255,0.8);
}


/* Soft moving glow */

.glow {
    position: absolute;
    width: 220px;
    height: 220px;
    border-radius: 50%;

    background: rgba(120,170,255,0.18);

    filter: blur(35px);

    animation: glowMove 7s ease-in-out infinite;
}

.glow.one {
    left: -60px;
    top: -60px;
}

.glow.two {
    right: -60px;
    bottom: -80px;

    background: rgba(190,130,255,0.18);

    animation-delay: 2s;
}


/* LEFT CONTENT */

.content {
    position: absolute;
    left: 7%;
    top: 55px;
    width: 45%;
    z-index: 5;
}

.tag {
    display: inline-block;

    padding: 7px 15px;

    border-radius: 30px;

    background: rgba(255,255,255,0.65);

    border: 1px solid rgba(255,255,255,0.9);

    font-size: 13px;
    font-weight: bold;

    color: #555;

    letter-spacing: 1px;

    animation: fadeUp 1s ease;
}

.title {
    margin-top: 18px;

    font-size: 42px;

    line-height: 1.08;

    font-weight: 800;

    color: #1e2430;

    animation: fadeUp 1.2s ease;
}

.highlight {
    background: linear-gradient(90deg, #536dfe, #9c6cff);

    -webkit-background-clip: text;

    -webkit-text-fill-color: transparent;
}

.description {
    margin-top: 16px;

    font-size: 16px;

    line-height: 1.6;

    color: #646b78;

    max-width: 430px;

    animation: fadeUp 1.4s ease;
}


/* BUTTON */

.button {
    display: inline-block;

    margin-top: 22px;

    padding: 13px 22px;

    border-radius: 12px;

    background: #202735;

    color: white;

    font-size: 14px;

    font-weight: bold;

    box-shadow: 0 10px 25px rgba(0,0,0,0.18);

    animation: fadeUp 1.6s ease;
}


/* RIGHT 3D SCENE */

.scene {
    position: absolute;

    right: 7%;
    top: 35px;

    width: 42%;
    height: 310px;

    perspective: 1000px;
}


/* Main apartment card */

.apartment {
    position: absolute;

    right: 35px;
    top: 35px;

    width: 285px;
    height: 210px;

    border-radius: 25px;

    background:
        linear-gradient(145deg, #ffffff, #e9ecf5);

    box-shadow:
        25px 30px 50px rgba(50,60,90,0.22);

    transform:
        rotateY(-12deg)
        rotateX(7deg);

    animation: apartmentFloat 4s ease-in-out infinite;

    border: 1px solid rgba(255,255,255,0.9);
}


/* Apartment roof */

.roof {
    position: absolute;

    left: 55px;
    top: -30px;

    width: 175px;
    height: 80px;

    background: linear-gradient(135deg, #667eea, #8e6cff);

    clip-path: polygon(50% 0%, 100% 70%, 92% 70%, 50% 18%, 8% 70%, 0% 70%);

    filter: drop-shadow(0 8px 10px rgba(70,70,150,0.25));
}


/* Windows */

.window {
    position: absolute;

    width: 48px;
    height: 55px;

    background: linear-gradient(135deg, #9edcff, #5aa8df);

    border-radius: 8px;

    top: 65px;

    box-shadow:
        inset 0 0 0 4px rgba(255,255,255,0.45);

    animation: windowGlow 3s ease-in-out infinite;
}

.window.left {
    left: 40px;
}

.window.right {
    right: 40px;
}


/* Door */

.door {
    position: absolute;

    width: 48px;
    height: 78px;

    bottom: 0;
    left: 118px;

    border-radius: 8px 8px 0 0;

    background: linear-gradient(135deg, #343b4a, #1e2430);
}


/* Floating rent card */

.price-card {
    position: absolute;

    right: -20px;
    bottom: 5px;

    width: 175px;

    padding: 16px;

    border-radius: 18px;

    background: rgba(255,255,255,0.92);

    backdrop-filter: blur(12px);

    box-shadow:
        0 15px 35px rgba(30,40,70,0.20);

    animation: priceFloat 3s ease-in-out infinite;
}

.price-label {
    font-size: 12px;
    color: #777;
}

.price {
    margin-top: 4px;

    font-size: 25px;

    font-weight: 800;

    color: #222;
}


/* Location badge */

.location {
    position: absolute;

    left: 15px;
    bottom: 30px;

    padding: 10px 16px;

    border-radius: 14px;

    background: rgba(255,255,255,0.75);

    backdrop-filter: blur(10px);

    font-size: 13px;

    font-weight: bold;

    color: #4d5360;

    box-shadow: 0 8px 20px rgba(0,0,0,0.08);

    animation: priceFloat 3.5s ease-in-out infinite;
}


/* ANIMATIONS */

@keyframes apartmentFloat {

    0%,100% {
        transform:
            rotateY(-12deg)
            rotateX(7deg)
            translateY(0);
    }

    50% {
        transform:
            rotateY(-12deg)
            rotateX(7deg)
            translateY(-12px);
    }
}


@keyframes priceFloat {

    0%,100% {
        transform: translateY(0);
    }

    50% {
        transform: translateY(-10px);
    }
}


@keyframes glowMove {

    0%,100% {
        transform: translate(0,0);
    }

    50% {
        transform: translate(50px,30px);
    }
}


@keyframes windowGlow {

    0%,100% {
        opacity: 0.75;
    }

    50% {
        opacity: 1;
    }
}


@keyframes fadeUp {

    from {
        opacity: 0;
        transform: translateY(20px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}
/* PREMIUM PROPERTY FORM */

.property-section {
    margin-top: 10px;
    padding: 25px;
    border-radius: 24px;
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.12);
    box-shadow: 0 15px 40px rgba(0,0,0,0.10);
}

.property-heading {
    font-size: 26px;
    font-weight: 750;
    margin-bottom: 5px;
}

.property-subheading {
    font-size: 14px;
    opacity: 0.65;
    margin-bottom: 22px;
}

.rent-highlight {
    margin-top: 22px;
    padding: 20px;
    border-radius: 18px;
    background: rgba(120,120,255,0.10);
    border: 1px solid rgba(130,120,255,0.20);
}

div[data-baseweb="select"] > div,
div[data-baseweb="input"] > div {
    border-radius: 12px !important;
}
</style>

</head>

<body>

<div class="hero">

    <div class="glow one"></div>
    <div class="glow two"></div>


    <div class="content">

        <div class="tag">
            📍 INDORE • STUDENT RENTALS
        </div>

        <div class="title">
            Find Your
            <br>
            <span class="highlight">Perfect Student Rental</span>
        </div>

        <div class="description">
            AI-powered fair rent estimation to help students
            find the right property at the right price.
        </div>

        <div class="button">
            ✨ Smart Rent Estimation
        </div>

    </div>


    <div class="scene">

        <div class="apartment">

            <div class="roof"></div>

            <div class="window left"></div>

            <div class="window right"></div>

            <div class="door"></div>

        </div>


        <div class="price-card">

            <div class="price-label">
                💰 Estimated Fair Rent
            </div>

            <div class="price">
                ₹12,500
            </div>

            <div class="price-label">
                per month
            </div>

        </div>


        <div class="location">
            📍 Indore
        </div>

    </div>

</div>

</body>
</html>
""", height=400)

# HEADER
# --------------------------------------------------



st.divider()

# --------------------------------------------------
# INPUT SECTION
# --------------------------------------------------

st.markdown("""
<div class="property-section">

    <div class="property-heading">
        🏡 Property Details
    </div>

    <div class="property-subheading">
        Tell us about the property to get an accurate fair-rent estimate.
    </div>

</div>
""", unsafe_allow_html=True)

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
