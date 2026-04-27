import streamlit as st
import joblib
import numpy as np
import plotly.graph_objects as go

# --- CONFIG ---
st.set_page_config(page_title="Churn Dashboard", layout="wide", page_icon="")

# --- CLEAN CSS (SAFE) ---
st.markdown("""
<style>

/* Background */
.main {
    background-color: #f5f7fb;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #ffffff;
    border-right: 1px solid #e5e7eb;
}

/* KPI Cards (ALL SAME STYLE) */
[data-testid="stMetric"] {
    background-color: #ffffff;
    border: 1px solid #e5e7eb;
    padding: 18px;
    border-radius: 14px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.06);
}

/* Section Containers */
.block-container {
    padding-top: 1rem;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(135deg, #4f46e5, #6366f1);
    color: white;
    border-radius: 8px;
    border: none;
    padding: 10px 14px;
    font-weight: 500;
}

/* Alerts */
.stAlert {
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# --- LOAD MODEL ---
@st.cache_resource
def load_assets():
    return joblib.load("scaler.pkl"), joblib.load("model.pkl")

try:
    scaler, model = load_assets()
except:
    st.error("⚠️ Missing model files.")
    st.stop()

# --- SIDEBAR (FILTER PANEL) ---
with st.sidebar:
    st.header("👤 Customer Controls")

    age = st.slider("Age", 18, 100, 30)
    gender = st.selectbox("Gender", ["Male", "Female"])
    tenure = st.slider("Tenure (months)", 0, 120, 12)
    monthly_charges = st.number_input("Monthly Charges ($)", 10.0, 500.0, 75.0)

    st.markdown("---")
    st.caption("Adjust inputs to update predictions")

# --- DATA PROCESSING ---
gender_val = 1 if gender == "Female" else 0
data = np.array([[age, gender_val, tenure, monthly_charges]])
scaled = scaler.transform(data)

prob = model.predict_proba(scaled)[0][1]

# --- STATUS ---
if prob < 0.3:
    status = "Healthy"
elif prob < 0.7:
    status = "Watchlist"
else:
    status = "High Risk"

# --- HEADER ---
st.title(" Customer Churn Intelligence Dashboard")
st.caption("Real-time predictive analytics for customer retention")

# =========================
# 🔷 KPI ROW
# =========================
k1, k2, k3 = st.columns(3)

k1.metric("Churn Probability", f"{prob*100:.1f}%")
k2.metric("Customer Status", status)
k3.metric("Monthly Value", f"${monthly_charges}")

st.divider()

# =========================
# 🔷 MAIN SECTION
# =========================
left, right = st.columns([2, 1])

# --- RISK VISUAL ---
with left:
    st.subheader(" Risk Overview")

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=prob * 100,
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "#4f46e5"},
            'steps': [
                {'range': [0, 30], 'color': '#d1fae5'},
                {'range': [30, 70], 'color': '#fef3c7'},
                {'range': [70, 100], 'color': '#fee2e2'}
            ]
        }
    ))

    fig.update_layout(height=350)
    st.plotly_chart(fig, use_container_width=True)

# --- ACTION PANEL ---
with right:
    st.subheader(" Action Center")

    if "offer" not in st.session_state:
        st.session_state.offer = False

    if prob > 0.7:
        st.error("🚨 High churn risk detected")

        if st.button(" Generate Retention Offer"):
            st.session_state.offer = True

        if st.session_state.offer:
            discount = "25%" if monthly_charges > 80 else "15%"
            st.success(f"Offer Ready: {discount} discount")

            if st.button("📩 Send Offer"):
                st.success("Offer sent successfully")
                st.session_state.offer = False

    elif prob > 0.4:
        st.warning("⚠️ Customer on watchlist")
    else:
        st.success("✅ Customer is stable")

# =========================
# 🔷 DETAILS SECTION
# =========================
st.divider()

with st.expander("📄 Customer Details"):
    st.json({
        "Age": age,
        "Gender": gender,
        "Tenure": f"{tenure} months",
        "Monthly Charges": f"${monthly_charges}"
    })

# --- VALIDATION ---
if tenure > age * 12:
    st.sidebar.warning("⚠️ Tenure exceeds realistic range")