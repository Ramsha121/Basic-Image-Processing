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



# -------------------- PAGE SETTINGS --------------------
st.set_page_config(
    page_title="Image Processing App",
    page_icon="🎨",
    layout="wide"
)
st.markdown("""
<h1 class='app-title'>🔥 Basic Image Processing Studio</h1>
""", unsafe_allow_html=True)
##--3 color gradient font 
st.markdown("""
<style>

    /* ================ 🔥 TITLE STYLING ================ */
    .app-title {
        text-align: center;
        font-size: 3rem;
        font-weight: 900;
        background: linear-gradient(90deg, #ff0000, #ff8800, #ffcc00);
        -webkit-background-clip: text;
        color: transparent;
        text-shadow: 0 0 20px rgba(255,80,0,0.6);
        margin-bottom: 20px;
        font-family: 'Segoe UI', sans-serif;
    }

    /* ================ 🔥 SIDEBAR BACKGROUND ================ */
    section[data-testid="stSidebar"] {
        background: #180000 !important;
        border-right: 2px solid #ff3300;
    }

    /* ================ 🔥 SIDEBAR RADIO LABELS ================ */
    section[data-testid="stSidebar"] .stRadio label {
        font-weight: 700 !important;
        font-size: 1.05rem !important;
        padding: 3px 0px;
        
        /* Fire Gradient Text 🎨 */
        background: linear-gradient(90deg, #ff3333, #ff9900, #ffcc33);
        -webkit-background-clip: text;
        color: transparent !important;

        text-shadow: 0px 0px 8px rgba(255,60,0,0.4);
    }

    /* ================ 🔥 SELECTED RADIO OPTION ================ */
    section[data-testid="stSidebar"] .stRadio div[role='radio'][aria-checked='true'] label {
        background: linear-gradient(90deg, #ff6600, #ffaa00, #ffee55);
        -webkit-background-clip: text;
        color: transparent !important;

        text-shadow: 0 0 10px rgba(255,150,0,0.8);
        font-size: 1.15rem !important;
    }

    /* Radio circle selected */
    section[data-testid="stSidebar"] .stRadio div[role='radio'][aria-checked='true'] svg {
        fill: #ff6600 !important;
        stroke: #ffcc00 !important;
    }

    /* Radio circle unselected */
    section[data-testid="stSidebar"] .stRadio div[role='radio'] svg {
        stroke: #ff6600 !important;
    }

    /* ================ 🔥 SIDEBAR TITLE ================ */
    section[data-testid="stSidebar"] h2 {
        text-align: center;
        font-weight: 900 !important;
        margin-bottom: 15px;

        background: linear-gradient(90deg, #ff3333, #ff9900, #ffee33);
        -webkit-background-clip: text;
        color: transparent !important;

        text-shadow: 0 0 12px rgba(255,80,0,0.8);
    }

    /* Hover Glow */
    section[data-testid="stSidebar"] .stRadio label:hover {
        text-shadow: 0 0 12px rgba(255,130,0,0.9);
        cursor: pointer;
    }

</style>
""", unsafe_allow_html=True)


# -------------------- CUSTOM PAGE THEME 🎨 --------------------
st.markdown("""
<style>

    /* 🎨 Make ALL sidebar radio labels visible (change font color) */
    section[data-testid="stSidebar"] .stRadio label {
        color: red !important;        /* change to any color you want */
        font-weight: 600 !important;
    }

    /* 🎨 Make selected option also red */
    section[data-testid="stSidebar"] .stRadio div[role='radio'] > div[data-testid='stMarkdownContainer'] {
        color: red !important;
        font-weight: 700 !important;
    }

    /* 🎨 Make "Choose an Option 👇" title red */
    section[data-testid="stSidebar"] h2 {
        color: red !important;
        font-weight: 800 !important;
    }

</style>
""", unsafe_allow_html=True)



# -------------------- SIDE MENU WITH FIXED LABELS --------------------
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

# -------------------- STOP IF NO IMAGE --------------------
if uploaded_file is None:
    st.info("⬅️ Please upload an image from the **sidebar** to continue.")
    st.stop()

# -------------------- LOAD IMAGE --------------------
image = Image.open(uploaded_file)
img_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
w, h = image.size


# -------------------- DOWNLOAD BUTTON FUNCTION --------------------
def download_image(img, filename):
    buf = BytesIO()
    img.save(buf, format="PNG")
    st.download_button("📥 Download Image", buf.getvalue(), file_name=filename)

##--CSS--
st.markdown("""
<style>

    /* ===================================================
       🔥🔥🔥 GLOBAL FIRE RED THEME — FULL APP 🔥🔥🔥
       =================================================== */

    /* ------ PAGE BACKGROUND ------ */
    .main {
        background-color: #0d0000 !important;  /* deep black/red */
        color: #ff4d4d !important;
    }

    /* ------ HEADINGS ------ */
    h1, h2, h3, h4, h5, h6 {
        color: #ff3333 !important;
        text-shadow: 0 0 10px #ff1a1a;
        font-weight: 900 !important;
    }

    /* ------ NORMAL TEXT ------ */
    p, span, li, label {
        color: #ff6666 !important;
    }

    /* ------ SIDEBAR BG ------ */
    section[data-testid="stSidebar"] {
        background-color: #1a0000 !important;
        border-right: 2px solid #ff1a1a;
    }

    /* ------ SIDEBAR HEADER ------ */
    section[data-testid="stSidebar"] h2 {
        color: #ff3333 !important;
        font-weight: 900 !important;
        text-shadow: 0px 0px 8px #ff0000;
    }

    /* ------ SIDEBAR RADIO LABELS ------ */
    section[data-testid="stSidebar"] .stRadio label {
        color: #ff4d4d !important;
        font-weight: 650 !important;
        text-shadow: 0px 0px 6px #b30000;
    }

    /* Selected radio label */
    section[data-testid="stSidebar"] .stRadio div[role='radio'][aria-checked='true'] label {
        color: #ff8080 !important;
        font-weight: 900 !important;
        text-shadow: 0px 0px 12px #ff3333;
    }

    /* Radio circle colors */
    section[data-testid="stSidebar"] .stRadio div[role='radio'][aria-checked='true'] svg {
        fill: #ff3333 !important;
        stroke: #ff3333 !important;
    }
    section[data-testid="stSidebar"] .stRadio div[role='radio'] svg {
        stroke: #ff1a1a !important;
    }

    /* Radio label hover */
    section[data-testid="stSidebar"] .stRadio label:hover {
        color: #ff9999 !important;
        text-shadow: 0 0 14px #ff4d4d;
        cursor: pointer;
    }

    /* ------ BUTTONS ------ */
    .stButton>button {
        background-color: #ff1a1a !important;
        color: white !important;
        border-radius: 10px !important;
        padding: 10px 22px !important;
        border: 1px solid #ff6666 !important;
        box-shadow: 0 0 12px #ff1a1a;
    }
    .stButton>button:hover {
        background-color: #ff3333 !important;
        box-shadow: 0 0 20px #ff4d4d;
    }

    /* ------ SLIDER ------ */
    .stSlider > div[data-baseweb="slider"] > div > div {
        background: #ff1a1a !important;
    }
    .stSlider > div[data-baseweb="slider"] > div > div > div {
        background: #ff3333 !important;
        box-shadow: 0 0 10px #ff4d4d;
    }

    /* ------ INPUT FIELDS ------ */
    input, textarea {
        border: 1px solid #ff1a1a !important;
        background-color: #330000 !important;
        color: #ff6666 !important;
    }

    /* ------ IMAGE GLOW ------ */
    img {
        border: 3px solid #ff1a1a !important;
        box-shadow: 0 0 15px #ff1a1a;
        border-radius: 8px;
    }

</style>
""", unsafe_allow_html=True)

# ====================== HOME ======================
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


# ====================== IMAGE PROPERTIES ======================
elif menu == "props":
    st.title("📏 Image Properties")

    col1, col2 = st.columns(2)
    with col1:
        st.image(image, caption="Uploaded Image", use_column_width=True)
    with col2:
        st.write(f"🖼 **Size:** {w} × {h}")
        st.write(f"🎯 **Mode:** {image.mode}")
        st.write(f"🔍 **Shape:** {np.array(img_cv).shape}")


# ====================== GRAYSCALE ======================
elif menu == "gray":
    st.title("⚫ Grayscale Image")

    gray_img = Image.fromarray(gray)
    st.image(gray_img, caption="Grayscale", use_column_width=True)
    download_image(gray_img, "grayscale.png")


# ====================== ROTATE ======================
elif menu == "rotate":
    st.title("🔄 Rotate Image")

    angle = st.radio("Choose rotation:", [90, 180, 270], horizontal=True)
    rotated = image.rotate(angle, expand=True)

    st.image(rotated, caption=f"Rotated {angle}°", use_column_width=True)
    download_image(rotated, f"rotated_{angle}.png")


# ====================== MIRROR ======================
elif menu == "mirror":
    st.title("🪞 Mirror Image")

    mirrored = image.transpose(Image.FLIP_LEFT_RIGHT)
    st.image(mirrored, caption="Mirrored Image", use_column_width=True)
    download_image(mirrored, "mirrored.png")


# ====================== CONTOURS ======================
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


# ====================== 50/50 SPLIT ======================
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


# ====================== CUSTOM PERCENT SPLIT ======================
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


# ====================== 4×4 GRID ======================
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

