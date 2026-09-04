import streamlit as st
import pandas as pd
import joblib
import os
import glob
from urllib.parse import quote

# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "student_rent_model.pkl")
model = joblib.load(MODEL_PATH)

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="RENTIQ Indore | Student Rental AI",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --------------------------------------------------
# GLOBAL CSS
# --------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --bg: #070812;
    --panel: #0e1020;
    --panel2: #121528;
    --text: #f6f7fb;
    --muted: #9da3b8;
    --line: rgba(255,255,255,.09);
    --purple: #8b5cf6;
    --blue: #4f8cff;
    --cyan: #4fd1ff;
}

.stApp {
    background:
        radial-gradient(circle at 15% 0%, rgba(111,72,255,.16), transparent 28%),
        radial-gradient(circle at 90% 12%, rgba(57,141,255,.12), transparent 25%),
        var(--bg);
    color: var(--text);
    font-family: 'Inter', sans-serif;
}

.block-container {
    max-width: 1250px;
    padding-top: 1rem;
    padding-bottom: 3rem;
}

/* hide Streamlit chrome */
#MainMenu, footer, header {visibility: hidden;}

/* NAVBAR */
.navbar {
    display:flex;
    align-items:center;
    justify-content:space-between;
    padding:14px 4px 22px;
    margin-bottom:8px;
}
.nav-brand {
    display:flex;
    align-items:center;
    gap:10px;
    font-weight:800;
    letter-spacing:.5px;
    font-size:19px;
}
.brand-mark {
    width:38px;
    height:38px;
    border-radius:12px;
    display:flex;
    align-items:center;
    justify-content:center;
    background:linear-gradient(135deg,#8b5cf6,#4f8cff);
    box-shadow:0 8px 25px rgba(107,92,246,.35);
}
.nav-right {color:#aeb4c7;font-size:13px;}

/* HERO */
.hero {
    position:relative;
    overflow:hidden;
    min-height:430px;
    border:1px solid var(--line);
    border-radius:32px;
    padding:54px 58px;
    background:
        radial-gradient(circle at 76% 25%, rgba(111,92,246,.26), transparent 25%),
        radial-gradient(circle at 92% 75%, rgba(55,155,255,.16), transparent 25%),
        linear-gradient(135deg,#0e1120,#11142a 55%,#0d1020);
    box-shadow:0 30px 90px rgba(0,0,0,.35), inset 0 1px 0 rgba(255,255,255,.04);
}
.hero:before,.hero:after {
    content:"";position:absolute;border-radius:50%;filter:blur(1px);pointer-events:none;
}
.hero:before {width:260px;height:260px;left:-130px;top:-140px;background:rgba(126,92,246,.15);}
.hero:after {width:200px;height:200px;right:-80px;bottom:-100px;background:rgba(61,145,255,.12);}
.hero-grid {display:grid;grid-template-columns:1.08fr .92fr;gap:30px;position:relative;z-index:2;}
.eyebrow {
    display:inline-flex;align-items:center;gap:8px;padding:8px 13px;border-radius:30px;
    background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.10);
    color:#cdd2e4;font-size:11px;font-weight:700;letter-spacing:1.1px;
}
.hero-title {font-size:54px;line-height:1.02;font-weight:800;margin:20px 0 16px;letter-spacing:-2px;}
.hero-title span {background:linear-gradient(90deg,#a78bfa,#60a5fa);-webkit-background-clip:text;color:transparent;}
.hero-copy {max-width:550px;color:#aeb4c7;font-size:15px;line-height:1.7;}
.hero-pills {display:flex;gap:10px;flex-wrap:wrap;margin-top:24px;}
.hero-pill {padding:9px 12px;border:1px solid var(--line);border-radius:12px;background:rgba(255,255,255,.045);font-size:12px;color:#c8ccda;}

/* BUILDING */
.scene {height:315px;position:relative;perspective:1000px;}
.building {
    position:absolute;right:50px;top:30px;width:245px;height:215px;border-radius:18px 18px 10px 10px;
    background:linear-gradient(145deg,#e8ecf7,#9da8c4);box-shadow:28px 32px 55px rgba(0,0,0,.35);
    transform:rotateY(-13deg) rotateX(5deg);animation:float 4.5s ease-in-out infinite;
}
.building:before {content:"";position:absolute;left:28px;right:28px;top:-55px;height:75px;background:linear-gradient(135deg,#8b5cf6,#4f8cff);clip-path:polygon(50% 0,100% 72%,90% 72%,50% 20%,10% 72%,0 72%);filter:drop-shadow(0 10px 12px rgba(92,79,205,.35));}
.window {position:absolute;width:43px;height:48px;border-radius:7px;background:linear-gradient(145deg,#79d7ff,#3972c8);box-shadow:inset 0 0 0 3px rgba(255,255,255,.28),0 0 20px rgba(79,209,255,.18);}
.w1{left:30px;top:52px}.w2{right:30px;top:52px}.w3{left:30px;top:119px}.w4{right:30px;top:119px}
.door {position:absolute;width:47px;height:80px;bottom:0;left:99px;border-radius:8px 8px 0 0;background:linear-gradient(145deg,#30384d,#141827);}
.door:after{content:"";position:absolute;right:7px;top:42px;width:5px;height:5px;border-radius:50%;background:#d4b16b;}
.ground {position:absolute;bottom:22px;right:4px;width:315px;height:24px;border-radius:50%;background:rgba(77,100,160,.22);filter:blur(10px);}

/* HERO RENT CARD */
.hero-rent {
    position:absolute;right:5px;bottom:25px;width:190px;padding:16px 18px;border-radius:18px;
    background:rgba(18,21,40,.88);border:1px solid rgba(255,255,255,.12);backdrop-filter:blur(15px);
    box-shadow:0 18px 45px rgba(0,0,0,.28);animation:float2 3.2s ease-in-out infinite;
}
.hero-rent small{color:#9299ad;font-size:11px}.hero-rent strong{display:block;font-size:23px;margin-top:4px;color:#fff;}
.hero-location{position:absolute;left:10px;bottom:18px;padding:9px 12px;border-radius:12px;background:rgba(255,255,255,.06);border:1px solid var(--line);font-size:11px;color:#bdc4d5;}

/* SECTION */
.section-head {display:flex;align-items:end;justify-content:space-between;margin:58px 0 18px;}
.section-kicker {font-size:11px;color:#8d95aa;letter-spacing:1.4px;font-weight:800;}
.section-title {font-size:28px;font-weight:800;margin-top:5px;letter-spacing:-.5px;}
.section-desc {font-size:13px;color:#8f96aa;margin-top:5px;}

/* HOW IT WORKS */
.steps {display:grid;grid-template-columns:repeat(3,1fr);gap:15px;}
.step {padding:22px;border:1px solid var(--line);border-radius:20px;background:linear-gradient(145deg,rgba(255,255,255,.045),rgba(255,255,255,.018));position:relative;overflow:hidden;}
.step-number{font-size:11px;color:#8e78ff;font-weight:800;letter-spacing:1px}.step-icon{font-size:27px;margin:13px 0 8px}.step h4{margin:0 0 6px;font-size:16px}.step p{margin:0;color:#8e95a9;font-size:12px;line-height:1.6;}

/* PROPERTY PANEL */
.property-panel {padding:28px;border:1px solid var(--line);border-radius:26px;background:linear-gradient(145deg,rgba(255,255,255,.045),rgba(255,255,255,.018));box-shadow:0 25px 60px rgba(0,0,0,.16);}
.panel-top {display:flex;justify-content:space-between;align-items:center;margin-bottom:20px;}
.panel-title{font-size:20px;font-weight:800}.panel-badge{font-size:10px;color:#b7bdf0;padding:7px 10px;border-radius:20px;background:rgba(139,92,246,.12);border:1px solid rgba(139,92,246,.22);}

/* STREAMLIT INPUTS */
div[data-testid="stSelectbox"] label,
div[data-testid="stNumberInput"] label {color:#b8bfd0 !important;font-size:12px !important;font-weight:600 !important;}
div[data-baseweb="select"] > div,
div[data-baseweb="input"] > div {background:#151829 !important;border:1px solid rgba(255,255,255,.08) !important;border-radius:13px !important;min-height:45px !important;}
div[data-baseweb="select"] > div:hover,
div[data-baseweb="input"] > div:hover {border-color:rgba(139,92,246,.55) !important;box-shadow:0 0 0 2px rgba(139,92,246,.08) !important;}
input {color:#f6f7fb !important;}

/* RENT INPUT */
.rent-input-wrap {margin-top:16px;padding:18px 20px;border-radius:18px;background:linear-gradient(135deg,rgba(139,92,246,.12),rgba(79,140,255,.08));border:1px solid rgba(139,92,246,.20);}

/* BUTTON */
.stButton > button {border:0 !important;border-radius:14px !important;background:linear-gradient(90deg,#7c5cff,#4f8cff) !important;color:white !important;font-weight:800 !important;min-height:52px !important;box-shadow:0 12px 30px rgba(89,84,246,.25) !important;transition:.25s !important;}
.stButton > button:hover {transform:translateY(-2px);box-shadow:0 17px 36px rgba(89,84,246,.35) !important;}

/* RESULTS */
.result-grid {display:grid;grid-template-columns:repeat(3,1fr);gap:15px;}
.metric-card {padding:22px;border:1px solid var(--line);border-radius:20px;background:linear-gradient(145deg,rgba(255,255,255,.055),rgba(255,255,255,.018));}
.metric-label{font-size:11px;color:#9299ad;text-transform:uppercase;letter-spacing:1px}.metric-value{font-size:30px;font-weight:800;margin-top:8px;color:#fff}.metric-sub{font-size:11px;color:#858ca0;margin-top:5px;}
.status {margin-top:16px;padding:18px 20px;border-radius:18px;border:1px solid var(--line);font-weight:700;}
.status.good{background:rgba(34,197,94,.09);border-color:rgba(34,197,94,.25);color:#86efac}.status.fair{background:rgba(234,179,8,.08);border-color:rgba(234,179,8,.22);color:#fde68a}.status.bad{background:rgba(239,68,68,.08);border-color:rgba(239,68,68,.22);color:#fca5a5}

/* METER */
.meter-card{margin-top:16px;padding:22px;border:1px solid var(--line);border-radius:20px;background:rgba(255,255,255,.025);}
.meter-head{display:flex;justify-content:space-between;font-size:12px;color:#a3aabd}.meter{height:12px;border-radius:20px;background:linear-gradient(90deg,#22c55e 0%,#eab308 50%,#ef4444 100%);margin:15px 0 8px;position:relative}.meter-dot{position:absolute;top:50%;width:22px;height:22px;border-radius:50%;background:white;border:4px solid #171a2c;transform:translate(-50%,-50%);box-shadow:0 0 18px rgba(255,255,255,.35);}

/* SUGGESTIONS */
.cards {display:grid;grid-template-columns:repeat(3,1fr);gap:15px;}
.property-card {padding:0;overflow:hidden;border:1px solid var(--line);border-radius:22px;background:linear-gradient(145deg,#101325,#0c0f1d);transition:.25s;}
.property-card:hover{transform:translateY(-5px);border-color:rgba(139,92,246,.4);box-shadow:0 18px 45px rgba(0,0,0,.25);}
.card-visual{height:120px;position:relative;background:radial-gradient(circle at 50% 10%,rgba(139,92,246,.25),transparent 45%),linear-gradient(135deg,#141a31,#0b0e1b);}
.mini-building{position:absolute;left:50%;bottom:10px;transform:translateX(-50%);width:115px;height:85px;border-radius:10px 10px 5px 5px;background:linear-gradient(145deg,#dbe3f4,#8793ae);box-shadow:12px 15px 25px rgba(0,0,0,.35);}
.mini-building:before{content:"";position:absolute;left:12px;right:12px;top:-25px;height:35px;background:#7156db;clip-path:polygon(50% 0,100% 70%,0 70%);}
.mini-window{position:absolute;width:18px;height:22px;background:#67c9ed;border-radius:3px;top:22px}.mw1{left:15px}.mw2{right:15px}.mini-door{position:absolute;bottom:0;left:48px;width:20px;height:34px;background:#273044;border-radius:4px 4px 0 0;}
.card-body{padding:16px}.card-top{display:flex;justify-content:space-between;gap:10px}.card-name{font-size:14px;font-weight:800}.deal{font-size:9px;padding:5px 7px;border-radius:10px;background:rgba(34,197,94,.10);color:#86efac;border:1px solid rgba(34,197,94,.16)}.card-meta{display:flex;gap:8px;flex-wrap:wrap;margin:10px 0;color:#858ca0;font-size:10px}.card-price{font-size:22px;font-weight:800}.card-price span{font-size:10px;color:#777f94;font-weight:500}

/* INQUIRY */
.inquiry {margin-top:55px;padding:30px;border-radius:26px;border:1px solid rgba(139,92,246,.18);background:radial-gradient(circle at 80% 20%,rgba(79,140,255,.12),transparent 28%),linear-gradient(135deg,rgba(139,92,246,.10),rgba(255,255,255,.025));}
.inquiry h3{font-size:24px;margin:0 0 6px}.inquiry p{color:#9299ad;font-size:13px;margin:0 0 20px}

.footer {margin-top:55px;padding-top:22px;border-top:1px solid var(--line);display:flex;justify-content:space-between;color:#70788e;font-size:10px;}

@keyframes float {0%,100%{transform:rotateY(-13deg) rotateX(5deg) translateY(0)}50%{transform:rotateY(-13deg) rotateX(5deg) translateY(-10px)}}
@keyframes float2 {0%,100%{transform:translateY(0)}50%{transform:translateY(-8px)}}

@media(max-width:850px){
    .hero{padding:35px 25px}.hero-grid{grid-template-columns:1fr}.scene{height:280px}.hero-title{font-size:40px}.building{right:50%;transform:translateX(50%) rotateY(-13deg) rotateX(5deg)}.hero-rent{right:0}.steps,.result-grid,.cards{grid-template-columns:1fr}.footer{display:block;line-height:2;}
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# NAVBAR
# --------------------------------------------------
st.markdown("""
<div class="navbar">
    <div class="nav-brand"><div class="brand-mark">🏠</div> RENTIQ INDORE</div>
    <div class="nav-right">AI Rental Intelligence&nbsp;&nbsp; • &nbsp;&nbsp;Student Focused</div>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HERO
# --------------------------------------------------
st.markdown("""
<div class="hero">
  <div class="hero-grid">
    <div>
      <div class="eyebrow">✦ AI-POWERED RENTAL ESTIMATION</div>
      <div class="hero-title">Find Your<br><span>Perfect Student Rental</span></div>
      <div class="hero-copy">Know what a property should cost before you rent it. Get a data-driven fair-rent estimate and discover better student-friendly options across Indore.</div>
      <div class="hero-pills">
        <div class="hero-pill">⚡ Instant Estimate</div>
        <div class="hero-pill">📊 Data Driven</div>
        <div class="hero-pill">🏠 Student Focused</div>
      </div>
    </div>
    <div class="scene">
      <div class="ground"></div>
      <div class="building">
        <div class="window w1"></div><div class="window w2"></div>
        <div class="window w3"></div><div class="window w4"></div>
        <div class="door"></div>
      </div>
      <div class="hero-rent"><small>💰 FAIR RENT PREVIEW</small><strong>₹12,500</strong><small>per month</small></div>
      <div class="hero-location">📍 Indore, Madhya Pradesh</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HOW IT WORKS
# --------------------------------------------------
st.markdown("""
<div class="section-head"><div><div class="section-kicker">SIMPLE • SMART • FAST</div><div class="section-title">How it works</div><div class="section-desc">Three steps from property details to a smarter rental decision.</div></div></div>
<div class="steps">
  <div class="step"><div class="step-number">01 / INPUT</div><div class="step-icon">🏠</div><h4>Enter Property Details</h4><p>Tell us the location, property type, size, sharing and other rental details.</p></div>
  <div class="step"><div class="step-number">02 / ANALYZE</div><div class="step-icon">🤖</div><h4>AI Analyses the Property</h4><p>The trained machine-learning model estimates what the rent should be.</p></div>
  <div class="step"><div class="step-number">03 / DECIDE</div><div class="step-icon">📈</div><h4>Compare & Decide</h4><p>See fair rent, price status and alternative properties close to your needs.</p></div>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# PROPERTY INPUTS
# --------------------------------------------------
st.markdown("""
<div class="section-head"><div><div class="section-kicker">01 / PROPERTY INFORMATION</div><div class="section-title">Tell us about the property</div><div class="section-desc">Use the details from the listing you are considering.</div></div><div class="panel-badge">● READY FOR ANALYSIS</div></div>
<div class="property-panel">
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    location = st.selectbox("📍 Location", [
        "Vijay Nagar", "Bhawarkua", "Rau", "Palasia", "Bengali Square",
        "Geeta Bhawan", "Sukhliya", "Scheme 54", "LIG Colony", "Bicholi Mardana"
    ])
    property_type = st.selectbox("🏢 Property Type", ["PG", "Single Room", "Shared Room", "1 BHK", "2 BHK"])
    area_sqft = st.number_input("📐 Area (sq.ft.)", min_value=50, max_value=3000, value=600)

with col2:
    bhk = st.selectbox("🛏️ BHK", [0, 1, 2])
    sharing = st.selectbox("👥 Sharing", ["Single", "Double", "Triple", "Whole Property"])
    bathrooms = st.selectbox("🚿 Bathrooms", [1, 2, 3])

with col3:
    attached_bathroom = st.selectbox("🚿 Attached Bathroom", ["Yes", "No"])
    distance_from_college_km = st.number_input("🎓 Distance from College (km)", min_value=0.1, max_value=20.0, value=1.5)
    security_deposit = st.number_input("💰 Security Deposit (₹)", min_value=0, max_value=100000, value=15000)

st.markdown('<div class="rent-input-wrap">', unsafe_allow_html=True)
listed_rent = st.number_input("🏷️ Listed Monthly Rent (₹)", min_value=1000, max_value=100000, value=12000, step=500)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.write("")
if st.button("✨  ESTIMATE FAIR RENT", use_container_width=True, type="primary"):
    # Keep compatibility with the currently deployed model. If the model was
    # retrained with fewer columns, feature_names_in_ automatically selects them.
    full_input = pd.DataFrame([{
        "location": location,
        "property_type": property_type,
        "area_sqft": area_sqft,
        "bhk": bhk,
        "sharing": sharing,
        "bathrooms": bathrooms,
        "furnishing": "Semi-Furnished",
        "parking": "No",
        "wifi": "Yes",
        "food": "No",
        "attached_bathroom": attached_bathroom,
        "distance_from_college_km": distance_from_college_km,
        "security_deposit": security_deposit,
    }])

    try:
        expected = getattr(model, "feature_names_in_", None)
        if expected is not None:
            usable = [c for c in expected if c in full_input.columns]
            input_data = full_input[usable]
        else:
            input_data = full_input
        fair_rent = round(float(model.predict(input_data)[0]))
    except Exception as e:
        st.error(f"Prediction could not be generated: {e}")
        st.stop()

    difference_percent = ((listed_rent - fair_rent) / fair_rent) * 100 if fair_rent else 0

    # --------------------------------------------------
    # RESULTS
    # --------------------------------------------------
    st.markdown("""
    <div class="section-head"><div><div class="section-kicker">02 / AI ANALYSIS</div><div class="section-title">Your rental intelligence</div><div class="section-desc">A quick comparison between the listing price and the model-estimated fair rent.</div></div></div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f'<div class="metric-card"><div class="metric-label">Listed Rent</div><div class="metric-value">₹{listed_rent:,}</div><div class="metric-sub">Current asking price</div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown(f'<div class="metric-card"><div class="metric-label">Estimated Fair Rent</div><div class="metric-value">₹{fair_rent:,}</div><div class="metric-sub">AI model estimate</div></div>', unsafe_allow_html=True)
    with c3:
        sign = "+" if difference_percent > 0 else ""
        st.markdown(f'<div class="metric-card"><div class="metric-label">Price Difference</div><div class="metric-value">{sign}{difference_percent:.1f}%</div><div class="metric-sub">Compared with fair rent</div></div>', unsafe_allow_html=True)

    if difference_percent > 10:
        status_class, status_text = "bad", "🔴 OVERPRICED — The listing is significantly above the estimated fair rent."
    elif difference_percent < -10:
        status_class, status_text = "good", "🟢 GOOD DEAL — The listing is below the estimated fair rent."
    else:
        status_class, status_text = "fair", "🟡 FAIR PRICE — The listing is close to the estimated fair rent."

    st.markdown(f'<div class="status {status_class}">{status_text}</div>', unsafe_allow_html=True)

    # meter position: -20% maps to 0, +20% maps to 100
    meter_pos = max(0, min(100, 50 + difference_percent * 2.5))
    st.markdown(f'''
    <div class="meter-card">
        <div class="meter-head"><span>GOOD DEAL</span><span>FAIR</span><span>OVERPRICED</span></div>
        <div class="meter"><div class="meter-dot" style="left:{meter_pos}%;"></div></div>
        <div class="meter-head"><span>Below market</span><span>Near estimated value</span><span>Above market</span></div>
    </div>
    ''', unsafe_allow_html=True)

    # --------------------------------------------------
    # SUGGESTIONS
    # --------------------------------------------------
    st.markdown("""
    <div class="section-head"><div><div class="section-kicker">03 / ALTERNATIVES</div><div class="section-title">Other better options</div><div class="section-desc">Properties closest to your estimated fair-rent range.</div></div></div>
    """, unsafe_allow_html=True)

    csv_files = glob.glob(os.path.join(BASE_DIR, "*.csv"))
    data_file = None
    for file in csv_files:
        name = os.path.basename(file).lower()
        if "rental" in name or "rent" in name:
            data_file = file
            break
    if data_file is None and csv_files:
        data_file = csv_files[0]

    if data_file:
        try:
            df = pd.read_csv(data_file)
            if "rent" not in df.columns:
                st.warning("Rental price column was not found in the dataset.")
            else:
                suggestions = df.copy()
                suggestions["rent"] = pd.to_numeric(suggestions["rent"], errors="coerce")
                suggestions = suggestions.dropna(subset=["rent"])
                similar = suggestions[(suggestions.get("location", pd.Series(index=suggestions.index)) == location) & (suggestions.get("property_type", pd.Series(index=suggestions.index)) == property_type)].copy()
                if len(similar) < 3 and "property_type" in suggestions.columns:
                    similar = suggestions[suggestions["property_type"] == property_type].copy()
                if len(similar) < 3:
                    similar = suggestions.copy()
                similar["rent_difference"] = (similar["rent"] - fair_rent).abs()
                similar = similar.sort_values("rent_difference").head(6)

                cards = []
                for i, (_, row) in enumerate(similar.iterrows(), start=1):
                    loc = str(row.get("location", "Indore"))
                    ptype = str(row.get("property_type", "Property"))
                    rent = int(row["rent"])
                    area = row.get("area_sqft", "—")
                    bhk_val = row.get("bhk", "—")
                    share = row.get("sharing", "—")
                    cards.append(f'''
                    <div class="property-card">
                        <div class="card-visual"><div class="mini-building"><div class="mini-window mw1"></div><div class="mini-window mw2"></div><div class="mini-door"></div></div></div>
                        <div class="card-body">
                            <div class="card-top"><div class="card-name">{ptype}</div><div class="deal">OPTION {i}</div></div>
                            <div class="card-meta"><span>📍 {loc}</span><span>📐 {area} sq.ft.</span><span>🛏️ BHK {bhk_val}</span><span>👥 {share}</span></div>
                            <div class="card-price">₹{rent:,} <span>/ month</span></div>
                        </div>
                    </div>
                    ''')
                st.markdown('<div class="cards">' + ''.join(cards) + '</div>', unsafe_allow_html=True)
        except Exception:
            st.warning("Alternative room suggestions could not be loaded.")
    else:
        st.info("Rental dataset not found in the repository.")

# --------------------------------------------------
# INQUIRY
# --------------------------------------------------
st.markdown("""
<div class="inquiry">
    <h3>Didn't find what you were looking for?</h3>
    <p>Send an inquiry and share the property details you need help with.</p>
</div>
""", unsafe_allow_html=True)

with st.form("inquiry_form"):
    q1, q2 = st.columns(2)
    with q1:
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
    with q2:
        phone = st.text_input("Phone Number")
        preferred = st.selectbox("Preferred Property", ["PG", "Single Room", "Shared Room", "1 BHK", "2 BHK"])
    message = st.text_area("Message", placeholder="Tell us what kind of student rental you are looking for...")
    submitted = st.form_submit_button("📩  SEND INQUIRY", use_container_width=True)

if submitted:
    body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nPreferred Property: {preferred}\n\nMessage:\n{message}"
    mailto = f"mailto:aayushnagar1743@gmail.com?subject={quote('RENTIQ Indore Rental Inquiry')}&body={quote(body)}"
    st.success("Inquiry details are ready. Tap the button below to open your email app.")
    st.markdown(f'<a href="{mailto}" target="_blank" style="display:inline-block;padding:12px 18px;border-radius:12px;background:linear-gradient(90deg,#7c5cff,#4f8cff);color:white;text-decoration:none;font-weight:700;">✉️ Open Email & Send</a>', unsafe_allow_html=True)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown("""
<div class="footer">
    <div>🏠 <b>RENTIQ INDORE</b> — AI-powered student rental intelligence.</div>
    <div>Built for student rental analysis • Indore, Madhya Pradesh</div>
</div>
""", unsafe_allow_html=True)
