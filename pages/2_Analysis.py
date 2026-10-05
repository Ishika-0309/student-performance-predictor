import streamlit as st
import matplotlib.pyplot as plt
from style import apply_css
apply_css()

st.set_page_config(
    page_title="Analysis",
    page_icon="📊",
    layout="centered"
)

st.markdown("""
<style>


.stApp {
    background: linear-gradient(135deg, #fbc2eb 0%, #a6c1ee 40%, #5f9cff 100%);
}


.summary-box {
    background: linear-gradient(135deg, #ffffff, #e0f2fe);
    padding: 25px;
    border-radius: 15px;
    font-size: 18px;
    text-align: center;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.2);
    color: black !important;
}

h1, h2, h3 {
    text-align: center;
    color: black;
}

div.stButton > button {
    display: block;
    margin: 30px auto;
    background: linear-gradient(135deg, #3b82f6, #06b6d4);
    color: white;
    padding: 10px 25px;
    border-radius: 12px;
    font-size: 16px;
    font-weight: bold;
    border: none;
    transition: 0.3s;
}


div.stButton > button:hover {
    background: linear-gradient(135deg, #2563eb, #0891b2);
    transform: scale(1.05);
}

</style>
""", unsafe_allow_html=True)


data = st.session_state.get("analysis_data", None)

if data is None:
    st.warning("No data found. Please go back and predict first.")
    st.stop()


st.header("Input Summary")

st.markdown(f"""
<div class="summary-box">
<b>Gender:</b> {data['gender']} <br>
<b>Race:</b> {data['race']} <br>
<b>Education:</b> {data['education']} <br>
<b>Lunch:</b> {data['lunch']} <br>
<b>Test Prep:</b> {data['test_prep']} <br><br>
<b>Math:</b> {data['math']} |
<b>Reading:</b> {data['reading']} |
<b>Writing:</b> {data['writing']}
</div>
""", unsafe_allow_html=True)


st.subheader("Model Comparison")

models = ["Linear Regression", "Random Forest"]
scores = [data["pred_lr"], data["pred_rf"]]

fig, ax = plt.subplots()

bars = ax.bar(models, scores)


for bar in bars:
    bar.set_linewidth(2)

ax.set_ylabel("Score")
ax.set_title("Model Prediction Comparison")


for i, v in enumerate(scores):
    ax.text(i, v + 1, f"{v:.2f}", ha='center', fontsize=12)

ax.grid(axis='y', linestyle='--', alpha=0.5)

st.pyplot(fig)


st.subheader("Score Distribution")

labels = ["Math", "Reading", "Writing"]
values = [data["math"], data["reading"], data["writing"]]

fig2, ax2 = plt.subplots()

ax2.pie(
    values,
    labels=labels,
    autopct=lambda p: f"{int(round(p/100*sum(values)))}",
    startangle=90,
    explode=(0.05, 0.05, 0.05),  
    shadow=True                  
)

ax2.axis('equal')

st.pyplot(fig2)


st.markdown("<br>", unsafe_allow_html=True)

if st.button("Back to Prediction"):
    st.switch_page("pages/1_Prediction.py")