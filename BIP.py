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
<h1 class='app-title'>🎨 Basic Image Processing Studio</h1>
""", unsafe_allow_html=True)

# -------------------- STYLING --------------------
st.markdown("""
<style>
/* ====== PAGE TITLE ====== */
.app-title {
    text-align: center;
    font-size: 3rem;
    font-weight: 900;
    background: linear-gradient(90deg, #ff7b00, #ffd500, #ff4500);
    -webkit-background-clip: text;
    color: transparent;
    text-shadow: 0 0 20px rgba(255,140,0,0.6);
    margin-bottom: 20px;
    font-family: 'Segoe UI', sans-serif;
}

/* ====== SIDEBAR ====== */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #3e1a00, #6b2e00, #a64d00) !important; 
    border-right: 2px solid #ffcc66;
    padding-top: 10px;
    padding-bottom: 20px;
}

section[data-testid="stSidebar"] h2 {
    text-align: center;
    font-weight: 900 !important;
    margin-bottom: 15px;
    background: linear-gradient(90deg, #ffb347, #ffcc33, #ff7b00);
    -webkit-background-clip: text;
    color: transparent !important;
    text-shadow: 0 0 12px rgba(255,180,0,0.8);
}

/* Sidebar radio labels */
section[data-testid="stSidebar"] .stRadio label {
    font-weight: 600 !important;
    font-size: 1.05rem !important;
    padding: 5px 0px;
    background: linear-gradient(90deg, #ffcc99, #ffb347, #ff9900);
    -webkit-background-clip: text;
    color: transparent !important;
    text-shadow: 0px 0px 5px rgba(255,200,120,0.4);
}

/* Selected radio option */
section[data-testid="stSidebar"] .stRadio div[role='radio'][aria-checked='true'] label {
    background: linear-gradient(90deg, #ffd700, #ffa500, #ff8c00);
    -webkit-background-clip: text;
    color: transparent !important;
    text-shadow: 0 0 12px rgba(255,180,0,0.8);
    font-size: 1.15rem !important;
}

/* Radio circle selected */
section[data-testid="stSidebar"] .stRadio div[role='radio'][aria-checked='true'] svg {
    fill: #ffa500 !important;
    stroke: #ffd700 !important;
}

/* Hover effect */
section[data-testid="stSidebar"] .stRadio label:hover {
    text-shadow: 0 0 15px rgba(255,200,100,0.8);
    cursor: pointer;
}

/* ====== PAGE BACKGROUND ====== */
.main {
    background: linear-gradient(135deg, #fff7f0, #fff3e0, #ffe6cc) !important;
    color: #333333 !important;
}

/* ====== HEADINGS ====== */
h1, h2, h3, h4, h5, h6 {
    color: #ff6600 !important;
    text-shadow: 0 0 8px #ffa500;
    font-weight: 900 !important;
}

/* ====== NORMAL TEXT ====== */
p, span, li, label {
    color: #6b3e0c !important;
}

/* ====== BUTTONS ====== */
.stButton>button {
    background: linear-gradient(90deg, #ff9900, #ffcc33) !important;
    color: #333 !important;
    border-radius: 12px !important;
    padding: 10px 25px !important;
    border: 1px solid #ffb347 !important;
    font-weight: 700;
    box-shadow: 0 0 15px rgba(255,180,0,0.5);
    transition: 0.3s ease;
}
.stButton>button:hover {
    background: linear-gradient(90deg, #ffcc33, #ffb347) !important;
    box-shadow: 0 0 25px rgba(255,200,100,0.6);
}

/* ====== SLIDER ====== */
.stSlider > div[data-baseweb="slider"] > div > div {
    background: #ff9900 !important;
}
.stSlider > div[data-baseweb="slider"] > div > div > div {
    background: #ffcc33 !important;
    box-shadow: 0 0 8px rgba(255,200,100,0.5);
}

/* ====== INPUT FIELDS ====== */
input, textarea {
    border: 1px solid #ff9900 !important;
    background-color: #fff3e0 !important;
    color: #6b3e0c !important;
    border-radius: 6px;
    padding: 5px;
}

/* ====== IMAGE STYLING ====== */
img {
    border: 3px solid #ffcc66 !important;
    box-shadow: 0 0 20px rgba(255,180,0,0.5);
    border-radius: 10px;
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

# -------------------- SIDE MENU --------------------
st.sidebar.title("📌 Image Processing Menu")
menu_options = {
    "🏠 Home": "home",
    "📏 Image Properties": "props",
    "⚫ Grayscale": "gray",
    "🔄 Rotate Image": "rotate",
    "🪞 Mirror Image": "mirror",
    "🟢 Contours": "contours",
    "✂ Vertical / Horizontal Cut": "cut",
    "📐 Custom Percentage Cut": "custom",
    "🔳 4×4 Grid Split": "grid"
}

menu_label = st.sidebar.radio("Choose an Option 👇", list(menu_options.keys()))
menu = menu_options[menu_label]

# -------------------- IMAGE UPLOADER --------------------
uploaded_file = st.sidebar.file_uploader("📤 Upload an image", type=["png", "jpg", "jpeg"])
if uploaded_file is None:
    st.info("⬅️ Please upload an image from the **sidebar** to continue.")
    st.stop()

# -------------------- LOAD IMAGE --------------------
image = Image.open(uploaded_file)
img_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
w, h = image.size

# -------------------- DOWNLOAD FUNCTION --------------------
def download_image(img, filename):
    buf = BytesIO()
    img.save(buf, format="PNG")
    st.download_button("📥 Download Image", buf.getvalue(), file_name=filename)
