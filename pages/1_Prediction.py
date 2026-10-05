import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
from style import apply_css

st.set_page_config(
    page_title="Prediction",
    page_icon="🎓",
    layout="centered"
)

apply_css(home=False)

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #fbc2eb 0%, #a6c1ee 40%, #5f9cff 100%);
}

label, .stMarkdown, .stText, p {
    color: black !important;
    font-weight: 600 !important;
    font-size: 18px !important;
}

.block-container {
    background: rgba(255, 255, 255, 0.15);
    padding: 30px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
}

.score-box {
    text-align: center;
    font-size: 36px;
    font-weight: bold;
    color: #1d4ed8;
    margin-top: 20px;
    background: rgba(255, 255, 255, 0.6);
    padding: 10px;
    border-radius: 12px;
}

.result-box {
    text-align: center;
    padding: 15px;
    border-radius: 12px;
    font-size: 22px;
    font-weight: bold;
    margin-top: 15px;
}

.excellent { background: #15803d; }
.good { background: #38bdf8; }
.average { background: #b45309; }
.poor { background: #ff0000; }

.analysis-box {
    padding: 15px;
    border-radius: 15px;
    background: rgba(255,255,255,0.7);
    text-align: center;
    font-size: 20px;
    margin-top: 10px;
}

.best-model {
    text-align: center;
    font-size: 22px;
    font-weight: bold;
    margin-top: 20px;
    color: green;
}

.lr-box {
    background: linear-gradient(135deg, #3b82f6, #06b6d4);
}


.rf-box {
       background: linear-gradient(135deg, #3b82f6, #06b6d4);
}


</style>
""", unsafe_allow_html=True)


data = joblib.load("models.pkl")
model1 = data["lr_model"]
model2 = data["rf_model"]
columns = data["columns"]
scaler = data["scaler"]

st.header("🎓 Student Performance Predictor")


gender = st.radio("Gender", ["Male", "Female"])
race = st.selectbox("Race / Ethnicity", ["Group A", "Group B", "Group C", "Group D", "Group E"])

education = st.selectbox(
    "Parental Level of Education",
    ["some high school", "high school", "some college",
     "associate's degree", "bachelor's degree", "master's degree"]
)

lunch = st.selectbox("Lunch Type", ["standard", "free/reduced"])
test_prep = st.selectbox("Test Preparation Course", ["none", "completed"])


def validate_score(value, name):
    if value.strip() == "":
        return None, f"{name} is required"
    try:
        val = int(value)
        if val < 0 or val > 100:
            return None, f"{name} must be between 0 and 100"
        return val, None
    except:
        return None, f"{name} must be a number"


math_input = st.text_input("Math Score",value=0)
math, err1 = validate_score(math_input, "Math Score")
if err1:
    st.error(err1)

reading_input = st.text_input("Reading Score",value=0)
reading, err2 = validate_score(reading_input, "Reading Score")
if err2:
    st.error(err2)

writing_input = st.text_input("Writing Score",value=0)
writing, err3 = validate_score(writing_input, "Writing Score")
if err3:
    st.error(err3)


if st.button("Predict Score"):

    if None in (math, reading, writing):
        st.warning(" Enter valid scores (0-100)")
    else:
        df = pd.DataFrame({
            "gender": [gender],
            "race/ethnicity": [race],
            "parental level of education": [education],
            "lunch": [lunch],
            "test preparation course": [test_prep],
            "math score": [math],
            "reading score": [reading],
            "writing score": [writing]
        })

        df = pd.get_dummies(df)
        df = df.reindex(columns=columns, fill_value=0)

        st.session_state.pred_lr = model1.predict(scaler.transform(df))[0]
        st.session_state.pred_rf = model2.predict(df)[0]

        pred_lr = st.session_state.pred_lr
        pred_rf = st.session_state.pred_rf

        st.markdown(f'<div class="score-box">Predicted Score: {pred_lr:.2f}</div>', unsafe_allow_html=True)

        if pred_lr >= 85:
            st.markdown('<div class="result-box excellent">Excellent</div>', unsafe_allow_html=True)
        elif pred_lr >= 70:
            st.markdown('<div class="result-box good">Good</div>', unsafe_allow_html=True)
        elif pred_lr >= 50:
            st.markdown('<div class="result-box average">Average</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="result-box poor">Poor</div>', unsafe_allow_html=True)

    
        st.subheader(" Model Analysis")

        col1, col2 = st.columns(2)

    
        with col1:
            st.markdown(f"""
            <div class="analysis-box lr-box">
            <b>Linear Regression</b><br><br>
            Predicted Score: {pred_lr:.2f}
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <div class="analysis-box rf-box">
            <b>Random Forest</b><br><br>
            Predicted Score: {pred_rf:.2f}
            </div>
            """, unsafe_allow_html=True)

       
        math_val = float(math)
        reading_val = float(reading)
        writing_val = float(writing)

        avg_score = (math_val + reading_val + writing_val) / 3

        diff_lr = abs(pred_lr - avg_score)
        diff_rf = abs(pred_rf - avg_score)

        if diff_lr < diff_rf:
            best = "Linear Regression"
        else:
            best = "Random Forest"

        st.markdown(f'<div class="best-model"> Best Model: {best}</div>', unsafe_allow_html=True)


col_left, col_right = st.columns([3, 2])

with col_right:
    if st.button("Further More Analysis"):
        if st.session_state.pred_lr is None:
                st.warning("Please predict first!")
        else:
            st.session_state["analysis_data"] = {
                    "gender": gender,
                    "race": race,
                    "education": education,
                    "lunch": lunch,
                    "test_prep": test_prep,
                    "math": math,
                    "reading": reading,
                    "writing": writing,
                    "pred_lr": st.session_state.pred_lr,
                    "pred_rf": st.session_state.pred_rf
                    }

            st.switch_page("pages/2_Analysis.py")
