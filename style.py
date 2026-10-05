import base64
import streamlit as st

def apply_css(home=False):
    if home:
        with open("bg4.jpeg", "rb") as f:
            data = base64.b64encode(f.read()).decode()

        background = f"""
        .stApp {{
            background-image: url("data:image/jpeg;base64,{data}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;

            /* dark overlay */
            background-color: rgba(0,0,0,0.5);
            background-blend-mode: darken;
        }}
        """
    else:
        background = """
        .stApp {
            background: linear-gradient(135deg, #667eea, #764ba2);
        }
        """

    st.markdown(f"""
    <style>

    {background}

    .main > div {{
        background: transparent !important;
    }}

    .block-container {{
        padding: 25px;
        border-radius: 15px;
        margin-top: 40px;
    }}
    
    h1, h2, h3 {{
        text-align: center;
        color: black !important;
        font-weight: bold;
    }}

    p {{
        text-align: center;
        color: white !important;
    }}

    label {{
        color: black !important;
        font-weight: 600;
    }}
    
    div[data-testid="stRadio"] label,
    div[data-testid="stSelectbox"] label,
    div[data-testid="stNumberInput"] label {{
        color: black !important;
        font-weight: 600;
    }}

    input, .stSelectbox div[data-baseweb="select"] {{
        border-radius: 10px !important;
    }}


    .stButton > button {{
        display: block;
        margin: 15px auto;
        width: 100% !important;;
        background: linear-gradient(90deg, #00f5ff, #00c6ff);
        color: black !important;
        padding: 12px;
        border-radius: 12px;
        font-weight: bold;
        border: none;
        font-size: 16px;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    }}

    .stButton > button:hover {{
        transform: scale(1.05);
        background: linear-gradient(90deg, #00c6ff, #0096c7);
    }}


    section[data-testid="stSidebar"] {{
        background: linear-gradient(180deg, #2563eb, #06b6d4);
    }}

    section[data-testid="stSidebar"] * {{
        color: white !important;
    }}

    section[data-testid="stSidebarNav"] a {{
        background: rgba(255,255,255,0.1);
        margin: 5px 10px;
        border-radius: 10px;
        padding: 8px;
    }}

    section[data-testid="stSidebarNav"] a:hover {{
        background: #06b6d4;
    }}

    section[data-testid="stSidebarNav"] a[aria-current="page"] {{
        background: #06b6d4;
        font-weight: bold;
    }}

    footer {{
        visibility: hidden;
    }}

    </style>
    """, unsafe_allow_html=True)