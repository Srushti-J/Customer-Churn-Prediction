# 📊 Customer Churn Prediction & Retention Intelligence Dashboard

An end-to-end Machine Learning + Streamlit application that predicts customer churn probability and provides actionable retention strategies in real-time.

---

## 🚀 Project Overview
Customer churn is a critical problem for subscription-based businesses. This project helps in:
- **Predicting** customer churn probability
- **Classifying** customers into risk categories
- **Generating** retention offers automatically
- **Visualizing** insights through an interactive dashboard

---

## 🧠 Features
- 📈 **Churn Prediction Model**: Built using Scikit-learn (Features: Age, Gender, Tenure, Monthly Charges).
- 📊 **Interactive Dashboard**: Real-time updates with a clean KPI-based UI.
- 🕒 **Visualizations**: Gauge chart visualization using Plotly for instant risk assessment.
- ⚠️ **Risk Segmentation**: 
    - **Healthy**: (<30%)
    - **Watchlist**: (30%–70%)
    - **High Risk**: (>70%)
- 🎯 **Retention Offer Generator**: Suggests discounts based on customer value to simulate real-world business decision-making.

---

## 🛠️ Tech Stack
- **Frontend**: Streamlit
- **Machine Learning**: Scikit-learn
- **Visualization**: Plotly
- **Model Storage**: Joblib
- **Language**: Python

---

## 📂 Dataset
- **Source**: Kaggle Telecom Customer Churn Dataset
- **Link**: [Telecom Customer Churn Insights](https://www.kaggle.com/datasets/abdullah0a/telecom-customer-churn-insights-for-analysis)

---

## 📂 Project Structure
```text
Customer-Churn-Dashboard/
│── app.py             # Main Streamlit application
│── model.pkl          # Pre-trained ML model
│── scaler.pkl         # Pre-trained data scaler
│── requirements.txt   # Project dependencies
│── README.md          # Project documentation
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/customer-churn-dashboard.git
cd customer-churn-dashboard
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
streamlit run app.py
```

---

## 🔍 How It Works
1. **Input**: User enters customer details (Age, Tenure, Charges) via the sidebar.
2. **Processing**: Data is scaled using the pre-trained `scaler.pkl`.
3. **Prediction**: The model predicts the churn probability.
4. **Display**: Dashboard shows the Churn %, Customer Status, and a Gauge Chart.
5. **Action**: If a customer is flagged as high risk, a retention offer is generated automatically based on their value.

---

## 📌 Retention Strategy Logic
*   **High-value customer + High risk** → 25% discount offer.
*   **Medium-value customer** → 15% discount offer.

---

## 🔮 Future Improvements
- Add advanced ML models like **XGBoost** or **Deep Learning**.
- Deploy on cloud platforms (**AWS / GCP / Azure**).
- Integrate **real-time databases** for persistent customer tracking.
- Add an **authentication system** for secure access.

---

## 👩‍💻 Author
**Srushti Joshi**

⭐ If you like this project, give it a star on GitHub and feel free to contribute!
