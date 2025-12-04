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

# -------------------- STYLING --------------------
st.markdown("""
<style>
/* ================ TITLE ================ */
.app-title {
    text-align: center;
    font-size: 3rem;
    font-weight: 900;
    background: linear-gradient(90deg, #ff7b00, #ffd500, #ff4500);
    -webkit-background-clip: text;
    color: transparent;
    text-shadow: 0 0 15px rgba(255,140,0,0.6);
    margin-bottom: 20px;
    font-family: 'Segoe UI', sans-serif;
}

/* ================ SIDEBAR ================ */
section[data-testid="stSidebar"] {
    background: #1a0b00 !important; /* dark warm brown */
    border-right: 2px solid #ffa500;
}

section[data-testid="stSidebar"] h2 {
    text-align: center;
    font-weight: 900 !important;
    margin-bottom: 15px;
    background: linear-gradient(90deg, #ff9900, #ffcc66, #ff6600);
    -webkit-background-clip: text;
    color: transparent !important;
    text-shadow: 0 0 12px rgba(255,160,0,0.8);
}

/* Sidebar radio labels */
section[data-testid="stSidebar"] .stRadio label {
    font-weight: 700 !important;
    font-size: 1.05rem !important;
    padding: 3px 0px;
    background: linear-gradient(90deg, #ffb347, #ffcc33, #ff7b00);
    -webkit-background-clip: text;
    color: transparent !important;
    text-shadow: 0px 0px 6px rgba(255,150,0,0.4);
}

/* Selected option */
section[data-testid="stSidebar"] .stRadio div[role='radio'][aria-checked='true'] label {
    background: linear-gradient(90deg, #ffd700, #ffa500, #ff8c00);
    -webkit-background-clip: text;
    color: transparent !important;
    text-shadow: 0 0 10px rgba(255,180,0,0.8);
    font-size: 1.15rem !important;
}

/* Radio circle selected */
section[data-testid="stSidebar"] .stRadio div[role='radio'][aria-checked='true'] svg {
    fill: #ffa500 !important;
    stroke: #ffd700 !important;
}

/* Radio circle unselected */
section[data-testid="stSidebar"] .stRadio div[role='radio'] svg {
    stroke: #ff8c00 !important;
}

/* Hover Glow */
section[data-testid="stSidebar"] .stRadio label:hover {
    text-shadow: 0 0 12px rgba(255,180,0,0.9);
    cursor: pointer;
}

/* ================ GLOBAL COLORS ================ */
.main {
    background-color: #fff7f0 !important;  /* soft warm cream */
    color: #333333 !important;
}

/* Headings */
h1, h2, h3, h4, h5, h6 {
    color: #ff6600 !important;
    text-shadow: 0 0 5px #ffa500;
    font-weight: 900 !important;
}

/* Normal text */
p, span, li, label {
    color: #6b3e0c !important;  /* warm brown */
}

/* Buttons */
.stButton>button {
    background-color: #ff9900 !important;
    color: white !important;
    border-radius: 10px !important;
    padding: 10px 22px !important;
    border: 1px solid #ffcc66 !important;
    box-shadow: 0 0 12px #ffcc66;
}
.stButton>button:hover {
    background-color: #ffcc33 !important;
    box-shadow: 0 0 20px #ffdd66;
}

/* Slider */
.stSlider > div[data-baseweb="slider"] > div > div {
    background: #ff9900 !important;
}
.stSlider > div[data-baseweb="slider"] > div > div > div {
    background: #ffcc33 !important;
    box-shadow: 0 0 10px #ffdd66;
}

/* Input fields */
input, textarea {
    border: 1px solid #ff9900 !important;
    background-color: #fff3e0 !important;
    color: #6b3e0c !important;
}

/* Image glow */
img {
    border: 3px solid #ffcc66 !important;
    box-shadow: 0 0 15px #ffcc66;
    border-radius: 8px;
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

# -------------------- FEATURES ---------------------
# Home
if menu == "home":
    st.title("🎨 Image Processing App")
    st.subheader("✨ Clean • Colorful • Easy-to-use ✨")
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
# Properties
elif menu == "props":
    st.title("📏 Image Properties")
    col1, col2 = st.columns(2)
    with col1:
        st.image(image, caption="Uploaded Image", use_column_width=True)
    with col2:
        st.write(f"🖼 **Size:** {w} × {h}")
        st.write(f"🎯 **Mode:** {image.mode}")
        st.write(f"🔍 **Shape:** {np.array(img_cv).shape}")

# Grayscale
elif menu == "gray":
    st.title("⚫ Grayscale Image")
    gray_img = Image.fromarray(gray)
    st.image(gray_img, caption="Grayscale", use_column_width=True)
    download_image(gray_img, "grayscale.png")

# Rotate
elif menu == "rotate":
    st.title("🔄 Rotate Image")
    angle = st.radio("Choose rotation:", [90, 180, 270], horizontal=True)
    rotated = image.rotate(angle, expand=True)
    st.image(rotated, caption=f"Rotated {angle}°", use_column_width=True)
    download_image(rotated, f"rotated_{angle}.png")

# Mirror
elif menu == "mirror":
    st.title("🪞 Mirror Image")
    mirrored = image.transpose(Image.FLIP_LEFT_RIGHT)
    st.image(mirrored, caption="Mirrored Image", use_column_width=True)
    download_image(mirrored, "mirrored.png")

# Contours
elif menu == "contours":
    st.title("🟢 Contour Detection")
    edges = cv2.Canny(gray, 100, 200)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contoured = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(contoured, contours, -1, (0,255,0), 2)
    contoured_img = Image.fromarray(cv2.cvtColor(contoured, cv2.COLOR_BGR2RGB))
    st.write(f"✨ **Contours Found:** {len(contours)}")
    col1, col2 = st.columns(2)
    col1.image(edges, caption="Edges", use_column_width=True)
    col2.image(contoured_img, caption="Contours", use_column_width=True)
    download_image(contoured_img, "contours.png")

# 50/50 Cut
elif menu == "cut":
    st.title("✂ Vertical & Horizontal 50/50 Cut")
    left = image.crop((0, 0, w//2, h))
    right = image.crop((w//2, 0, w, h))
    top = image.crop((0, 0, w, h//2))
    bottom = image.crop((0, h//2, w, h))
    st.subheader("📌 Vertical (Left / Right)")
    col1, col2 = st.columns(2)
    col1.image(left, caption="Left Half", use_column_width=True)
    col2.image(right, caption="Right Half", use_column_width=True)
    st.subheader("📌 Horizontal (Top / Bottom)")
    col3, col4 = st.columns(2)
    col3.image(top, caption="Top Half", use_column_width=True)
    col4.image(bottom, caption="Bottom Half", use_column_width=True)

# Custom Percentage Cut
elif menu == "custom":
    st.title("📐 Custom Percentage Cut")
    percent = st.slider("Select left side %:", 10, 90, 80)
    cut_x = int((percent / 100) * w)
    p1 = image.crop((0, 0, cut_x, h))
    p2 = image.crop((cut_x, 0, w, h))
    st.subheader(f"🔸 Left: {percent}%")
    st.image(p1)
    st.subheader(f"🔹 Right: {100 - percent}%")
    st.image(p2)

# 4x4 Grid
elif menu == "grid":
    st.title("🔳 4×4 Grid Split")
    grid_rows = 4
    grid_cols = 4
    tile_w = w // grid_cols
    tile_h = h // grid_rows
    tiles = []
    for r in range(grid_rows):
        for c in range(grid_cols):
            left = c * tile_w
            upper = r * tile_h
            right = (c+1)*tile_w if c < grid_cols-1 else w
            lower = (r+1)*tile_h if r < grid_rows-1 else h
            tiles.append(image.crop((left, upper, right, lower)))
    st.write("📦 **Generated 16 tiles:**")
    cols = st.columns(4)
    for i, tile in enumerate(tiles):
        cols[i % 4].image(tile, caption=f"Tile {i+1}", use_column_width=True)
