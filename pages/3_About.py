import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="👨‍💻",
    initial_sidebar_state="collapsed"
)

from style import apply_css
apply_css()


st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #fbc2eb 0%, #a6c1ee 40%, #5f9cff 100%);
}

.block-container {
    background: rgba(255, 255, 255, 0.15);
    padding: 30px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
}

h1, h2, h3, p, li {
    color: black !important;
    font-weight: 600;
    text-align: left;
}

.about-card {
    background: rgba(255,255,255,0.7);
    padding: 20px;
    border-radius: 12px;
    margin-top: 15px;
    color: black;
    font-size: 16px;
}

.model-box {
    padding: 15px;
    border-radius: 12px;
    margin-top: 10px;
    color: white;
    font-size: 16px;
}



.best {
    background: linear-gradient(135deg, #22c55e, #16a34a);
    color: white;
    text-align: center;
    font-weight: bold;
    font-size: 18px;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<h1 style='text-align: center; color: black;'>
About Student Performance Prediction System
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<div class="about-card">

<h3 style="text-align:center;"> About Project</h3>
<p>
This system predicts student performance using machine learning models based on various factors like gender, parental education, lunch type, and scores.
</p>

<hr>
<h3> Models Used</h3>


<h4> Linear Regression</h4>
<ul>
<li>Simple and fast algorithm</li>
<li>Finds linear relationship between input and output</li>
<li>Works well for basic predictions</li>
<li>Performs well when relationship is linear</li>
</ul>


<h4> Random Forest Regression</h4>
<ul>
<li>Advanced ensemble algorithm</li>
<li>Uses multiple decision trees</li>
<li>Handles complex relationships better</li>
<li>Provides higher accuracy</li>
<li>Less accurate when data is complex</li>
</ul>


<hr>
<h3> Purpose of the Project</h3>
<ul>
<li>Understand student performance factors</li>
<li>Provide early academic insights</li>
<li>Support data-driven decisions</li>
</ul>

<hr>
<h3> Technologies Used</h3>
<ul>
<li>Python</li>
<li>Pandas & NumPy</li>
<li>Scikit-learn</li>
<li>Streamlit</li>
<li>Joblib</li>
</ul>


<hr>
<h3> Developed By</h3>
<p>
Zeel Gohel<br>
Ishika Parmar<br>
Nehal Panchal
</p>

<hr>
<p>
This project demonstrates the practical use of Machine Learning in the education domain, helping bridge the gap between data and decision-making.
</p>
</div>
""", unsafe_allow_html=True)