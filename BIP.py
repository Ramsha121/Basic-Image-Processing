import streamlit as st
import cv2
import numpy as np
from PIL import Image
from io import BytesIO

# -------------------- PAGE SETTINGS --------------------
st.set_page_config(
    page_title="Image Processing App",
    page_icon="🎨",
    layout="wide"
)
st.markdown("""
<h1 class='app-title'>🔥 Basic Image Processing Studio</h1>
""", unsafe_allow_html=True)

# -------------------- TITLE STYLING --------------------
st.markdown("""
<style>
    /* ================ TITLE ================ */
    .app-title {
        text-align: center;
        font-size: 3rem;
        font-weight: 900;
        background: linear-gradient(90deg, #FF8C42, #FFB562, #FFD194);
        -webkit-background-clip: text;
        color: transparent;
        text-shadow: 0 0 15px rgba(255,180,120,0.5);
        margin-bottom: 20px;
        font-family: 'Segoe UI', sans-serif;
    }

    /* ================ SIDEBAR ================ */
    section[data-testid="stSidebar"] {
        background: #FFF3E0 !important;
        border-right: 2px solid #FFB562;
    }

    section[data-testid="stSidebar"] h2 {
        text-align: center;
        font-weight: 900 !important;
        background: linear-gradient(90deg, #FF8C42, #FFB562, #FFD194);
        -webkit-background-clip: text;
        color: transparent !important;
        text-shadow: 0 0 8px rgba(255,180,120,0.6);
    }

    section[data-testid="stSidebar"] .stRadio label {
        font-weight: 700 !important;
        font-size: 1rem !important;
        padding: 3px 0px;
        color: #6B4226 !important;
    }

    section[data-testid="stSidebar"] .stRadio div[role='radio'][aria-checked='true'] label {
        color: #A25C37 !important;
        font-weight: 800 !important;
    }

    section[data-testid="stSidebar"] .stRadio div[role='radio'][aria-checked='true'] svg {
        fill: #A25C37 !important;
        stroke: #D68C59 !important;
    }

    section[data-testid="stSidebar"] .stRadio div[role='radio'] svg {
        stroke: #B77B57 !important;
    }

    section[data-testid="stSidebar"] .stRadio label:hover {
        color: #D68C59 !important;
        text-shadow: 0 0 8px #D68C59;
        cursor: pointer;
    }

    /* ===================== GLOBAL ===================== */
    .main {
        background-color: #FFF8F0 !important;
        color: #3E2F2F !important;
    }

    h1, h2, h3, h4, h5, h6 {
        color: #3E2F2F !important;
        text-shadow: 0 0 5px rgba(200,150,120,0.3);
        font-weight: 900 !important;
    }

    p, span, li, label {
        color: #4A3B3B !important;
    }

    /* Buttons */
    .stButton>button {
        background-color: #FFB562 !important;
        color: #3E2F2F !important;
        border-radius: 10px !important;
        padding: 10px 22px !important;
        border: 1px solid #D68C59 !important;
        box-shadow: 0 0 8px #D68C59;
    }
    .stButton>button:hover {
        background-color: #FF8C42 !important;
        box-shadow: 0 0 12px #FFB562;
    }

    /* Sliders */
    .stSlider > div[data-baseweb="slider"] > div > div {
        background: #FFB562 !important;
    }
    .stSlider > div[data-baseweb="slider"] > div > div > div {
        background: #FF8C42 !important;
        box-shadow: 0 0 6px #FFB562;
    }

    /* Inputs */
    input, textarea {
        border: 1px solid #D68C59 !important;
        background-color: #FFF3E0 !important;
        color: #3E2F2F !important;
    }

    /* Images */
    img {
        border: 3px solid #FFB562 !important;
        box-shadow: 0 0 12px #FFD194;
        border-radius: 8px;
    }

    /* Animated gradient title */
    .animated-title {
        font-size: 3.2rem;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(90deg, #FF8C42, #FFB562, #FFD194, #FFB562, #FF8C42);
        background-size: 400% 400%;
        -webkit-background-clip: text;
        color: transparent;
        animation: warmFlow 6s ease infinite;
        text-shadow: 0 0 15px rgba(255,180,120,0.4);
        margin-bottom: 0.8rem;
    }

    @keyframes warmFlow {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Footer */
    .footer {
        text-align: center;
        margin-top: 40px;
        font-size: 1.15rem;
        font-weight: 700;
        color: #A25C37;
        text-shadow: 0 0 8px rgba(255,180,120,0.5);
    }

</style>
""", unsafe_allow_html=True)
