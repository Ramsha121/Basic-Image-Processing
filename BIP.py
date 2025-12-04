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
<h1 class='app-title'>✨ Basic Image Processing Studio</h1>
""", unsafe_allow_html=True)

# -------------------- WARM & AESTHETIC STYLING --------------------
st.markdown("""
<style>
/* ==================== PAGE TITLE ==================== */
.app-title {
    text-align: center;
    font-size: 3rem;
    font-weight: 900;
    background: linear-gradient(90deg, #FFAD60, #FFD280, #FFB347);
    -webkit-background-clip: text;
    color: transparent;
    text-shadow: 0 0 15px rgba(255,180,100,0.5);
    margin-bottom: 20px;
    font-family: 'Segoe UI', sans-serif;
}

/* ==================== SIDEBAR ==================== */
section[data-testid="stSidebar"] {
    background: linear-gradient(to bottom, #FFF0E0, #FFE0B2) !important;
    border-right: 2px solid #FFB347;
}

/* Sidebar Title */
section[data-testid="stSidebar"] h2 {
    text-align: center;
    font-weight: 900 !important;
    background: linear-gradient(90deg, #FFAD60, #FFD280);
    -webkit-background-clip: text;
    color: transparent !important;
    text-shadow: 0 0 10px rgba(255,180,100,0.7);
    margin-bottom: 15px;
}

/* Sidebar Radio Labels */
section[data-testid="stSidebar"] .stRadio label {
    font-weight: 600 !important;
    font-size: 1.05rem !important;
    background: linear-gradient(90deg, #FFD280, #FFB347, #FFAD60);
    -webkit-background-clip: text;
    color: transparent !important;
    text-shadow: 0px 0px 5px rgba(255,160,100,0.4);
}

/* Selected radio */
section[data-testid="stSidebar"] .stRadio div[role='radio'][aria-checked='true'] label {
    background: linear-gradient(90deg, #FFB347, #FFAD60, #FFD280);
    -webkit-background-clip: text;
    color: transparent !important;
    font-size: 1.15rem !important;
    text-shadow: 0 0 8px rgba(255,170,80,0.7);
}

/* Radio circle */
section[data-testid="stSidebar"] .stRadio div[role='radio'][aria-checked='true'] svg {
    fill: #FFAD60 !important;
    stroke: #FFB347 !important;
}
section[data-testid="stSidebar"] .stRadio div[role='radio'] svg {
    stroke: #FFAD60 !important;
}

/* Hover */
section[data-testid="stSidebar"] .stRadio label:hover {
    text-shadow: 0 0 10px rgba(255,180,120,0.7);
    cursor: pointer;
}

/* ==================== BUTTONS ==================== */
.stButton>button {
    background-color: #FFB347 !important;
    color: white !important;
    border-radius: 10px !important;
    border: 1px solid #FFD280 !important;
    box-shadow: 0 0 12px #FFAD60;
}
.stButton>button:hover {
    background-color: #FFD280 !important;
    box-shadow: 0 0 20px #FFB347;
}

/* ==================== SLIDERS ==================== */
.stSlider > div[data-baseweb="slider"] > div > div {
    background: #FFB347 !important;
}
.stSlider > div[data-baseweb="slider"] > div > div > div {
    background: #FFD280 !important;
    box-shadow: 0 0 10px #FFAD60;
}

/* ==================== INPUTS ==================== */
input, textarea {
    border: 1px solid #FFAD60 !important;
    background-color: #FFF5EB !important;
    color: #FF704D !important;
}

/* ==================== IMAGE ==================== */
img {
    border: 3px solid #FFD280 !important;
    box-shadow: 0 0 15px #FFB347;
    border-radius: 8px;
}

/* ==================== FOOTER ==================== */
.footer {
    text-align: center;
    margin-top: 40px;
    font-size: 1.15rem;
    font-weight: 700;
    color: #FFAD60;
    text-shadow: 0 0 8px rgba(255,180,100,0.6);
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

# -------------------- HOME --------------------
if menu == "home":
    st.title("🎨 Image Processing App")
    st.subheader("✨ Clean • Colorful • Warm & Easy-to-use ✨")
    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.markdown("""
    ### 🔧 Features You Can Use:
    - Grayscale  
    - Rotate  
    - Mirror  
    - Contours  
    - 50-50 Split  
    - Custom Percentage Split  
    - 4×4 Grid Tiles  
    👉 Choose a feature using the sidebar!
    """)

# (Other menu logic remains the same: props, gray, rotate, mirror, contours, cut, custom, grid)
