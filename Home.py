import streamlit as st
from style import apply_css

st.set_page_config(
    page_title="Student Predictor",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

apply_css(home=True)

st.markdown("""
<style>

.hero {
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    text-align: center;
    color: white;
}

.hero h1 {
    font-size: 50px;
    font-weight: 900;
    color: white !important;
}

.hero p {
    font-size: 20px;
    margin-top: 10px;
}

.scroll-down {
    margin-top: 25px;
    font-size: 18px;
    animation: bounce 1.5s infinite;
}

@keyframes bounce {
    0%,100% { transform: translateY(0); }
    50% { transform: translateY(10px); }
}

.section {
    padding: 80px 20px;
    display: flex;
    justify-content: center;
}

.overview-card {
    background: rgba(255, 255, 255, 0.2);
    backdrop-filter: blur(5px);
    padding: 30px;
    border-radius: 20px;
    width: 60%;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.2);
    border: 1px solid rgba(255,255,255,0.3);
    text-align: center;
}

.overview-card h3 {
    color: black !important;
    font-weight: 900;
    margin-bottom: 15px;
}

.overview-card p {
    color: black !important;
    font-weight: 600;
    font-size: 20px;
    line-height: 1.7;
}

div.stButton {
    display: flex;
    justify-content: center;
}

div.stButton > button {
    width: 280px !important;   
    height: 60px !important;   

    font-size: 20px !important;
    font-weight: 700;

    border-radius: 15px;
    border: none;

    color: white;

    background: linear-gradient(135deg, #667eea, #764ba2);

    box-shadow: 0px 10px 30px rgba(0,0,0,0.3);

    transition: all 0.3s ease;
}


div.stButton > button:hover {
    transform: translateY(-5px) scale(1.05);
}

div.stButton > button:active {
    transform: scale(0.95);
}

/* Center buttons spacing */
div[data-testid="column"] {
    padding: 10px;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>🎓 Student Performance Predictor</h1>
    <p>Predict • Analyze • Improve</p>
    <div class="scroll-down">⬇ Scroll Down</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section">
    <div class="overview-card">
        <h3>Overview</h3>
        <p>
        This system uses machine learning models like <b>Linear Regression</b> and <b>Random Forest</b> to predict student performance.  
        It helps understand how different factors impact academic results and provides accurate predictions.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)


st.markdown("<br><br>", unsafe_allow_html=True)


col1, col2, col3 = st.columns([1,2,1])

with col2:
    b1, b2 = st.columns(2)

    with b1:
        if st.button("Model", use_container_width=True):
            st.switch_page("pages/1_Prediction.py")

    with b2:
        if st.button("About", use_container_width=True):
            st.switch_page("pages/3_About.py")