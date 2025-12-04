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

# -------------------- FONT AND ANIMATION STYLING (GOLDEN THEME) --------------------
# Load Google Fonts (Playfair Display for titles, Poppins for text) and apply general styling
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Poppins:wght@300;400;600;700&display=swap');

/* ===================== GENERAL FONT AND COLOR ===================== */
/* Set default font for the entire app to Poppins */
html, body, [class*="st-emotion-cache"] {
    font-family: 'Poppins', sans-serif;
}

/* Set Main App Background */
.main {
    background-color: #FFFFFF !important; /* Pure white */
    color: #3B2F2F !important;
}

/* Headings Styling */
h1, h2, h3, h4, h5, h6 {
    font-family: 'Playfair Display', serif !important;
    color: #4B1F1F !important; /* Dark maroon/brown (for content headings) */
    text-shadow: 0 0 5px rgba(160,82,45,0.3) !important;
    font-weight: 800 !important; /* Bold headings */
    margin-top: 1rem;
    margin-bottom: 0.5rem;
}

/* General text (p, span, li, label) */
p, span, li, label, .stMarkdown {
    font-family: 'Poppins', sans-serif !important;
    color: #4B3B3B !important;
    font-weight: 400 !important;
}

/* ===================== HOME PAGE TITLE (GOLDEN) ===================== */
h1.app-title {
    font-family: 'Playfair Display', serif;
    font-size: 4.5rem; 
    font-weight: 900;
    text-align: center;
    /* --- NEW GOLDEN GRADIENT --- */
    background: linear-gradient(90deg, #FFD700, #FFA500, #FFD700, #DAA520); /* Gold, Orange, Yellow-Gold, Goldenrod */
    background-size: 200% 100%;
    -webkit-background-clip: text;
    color: transparent; /* Text uses gradient */
    text-shadow: 0 0 20px rgba(255, 215, 0, 0.8); /* Luminous golden shadow */
    animation: goldFlow 6s ease infinite; 
    margin-bottom: 5px; 
    letter-spacing: 2px;
}

@keyframes goldFlow {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* ===================== HOME PAGE SUBTITLE ===================== */
h2.app-subtitle {
    font-family: 'Poppins', sans-serif; 
    font-size: 2rem;
    font-weight: 600; 
    text-align: center;
    /* Retain original accent color for contrast */
    background: linear-gradient(90deg, #6E3B3B, #A0522D); 
    -webkit-background-clip: text;
    color: transparent;
    text-shadow: 0 0 8px rgba(160,82,45,0.5);
    margin-bottom: 30px; 
    letter-spacing: 1px;
}

/* ===================== SIDEBAR ===================== */
section[data-testid="stSidebar"] {
    background: #FFFBF7 !important; 
    border-right: 3px solid #A0522D; 
    box-shadow: 4px 0 15px rgba(0, 0, 0, 0.1);
}

/* Sidebar Title */
section[data-testid="stSidebar"] h2 {
    font-family: 'Playfair Display', serif !important;
    font-size: 1.8rem;
    text-align: center;
    font-weight: 900 !important;
    /* Sidebar title accent */
    background: linear-gradient(90deg, #800000, #A0522D); 
    -webkit-background-clip: text;
    color: transparent !important;
    text-shadow: 0 0 10px rgba(128, 0, 0, 0.7);
    padding: 15px 0;
    margin-top: 0;
    margin-bottom: 20px;
}

/* Sidebar Radio Buttons (Menu) */
section[data-testid="stSidebar"] .stRadio label {
    font-weight: 500 !important;
    font-size: 1.05rem !important;
    padding: 5px 10px;
    color: #3B2F2F !important;
    transition: all 0.2s ease;
}

/* Selected Radio Button */
section[data-testid="stSidebar"] .stRadio div[role='radio'][aria-checked='true'] label {
    color: #A0522D !important; /* Sienna for selected item */
    font-weight: 700 !important;
    background-color: #FFEDE5; 
    border-radius: 5px;
    padding: 5px 10px;
}

section[data-testid="stSidebar"] .stRadio div[role='radio'][aria-checked='true'] svg {
    fill: #A0522D !important;
    stroke: #800000 !important;
}

section[data-testid="stSidebar"] .stRadio div[role='radio'] svg {
    stroke: #A0522D !important;
}

section[data-testid="stSidebar"] .stRadio label:hover {
    color: #A0522D !important;
    text-shadow: 0 0 5px #A0522D;
    cursor: pointer;
}

/* ===================== ALERT BOXES & UPLOADER ===================== */
/* File Uploader button */
.stFileUploader {
    border: 1px solid #A0522D;
    padding: 10px;
    border-radius: 10px;
    background-color: #FFFDFB;
}

/* Info Box */
.stAlert > div[role="alert"] {
    background-color: #FFFCF7; 
    border-left: 5px solid #A0522D !important; /* Sienna alert border */
    border-radius: 5px;
}


/* ===================== BUTTONS ===================== */
.stButton>button, .stDownloadButton>button {
    font-family: 'Poppins', sans-serif !important;
    font-weight: 600 !important;
    background-color: #A0522D !important; /* Sienna Button */
    color: #FFF !important; 
    border-radius: 8px !important;
    padding: 8px 20px !important;
    border: none !important;
    box-shadow: 0 4px 10px rgba(160, 82, 45, 0.5);
    transition: all 0.2s ease;
}
.stButton>button:hover, .stDownloadButton>button:hover {
    background-color: #800000 !important; 
    box-shadow: 0 6px 15px rgba(128, 0, 0, 0.7);
    transform: translateY(-2px);
}

/* ===================== SLIDERS ===================== */
.stSlider > div[data-baseweb="slider"] > div > div {
    background: #FFDAB9 !important; 
}
.stSlider > div[data-baseweb="slider"] > div > div > div {
    background: #A0522D !important; /* Sienna Slider Thumb */
    box-shadow: 0 0 8px #A0522D;
}

/* ===================== IMAGES ===================== */
img {
    border: 5px solid #FFDAB9 !important; 
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2); 
    border-radius: 12px; 
    transition: transform 0.3s ease;
}

/* ===================== FOOTER ===================== */
.footer {
    text-align: center;
    margin-top: 50px;
    padding-top: 15px;
    border-top: 1px dashed #A0522D;
    font-size: 1.1rem;
    font-weight: 600;
    color: #6E3B3B;
    text-shadow: 0 0 5px rgba(160,82,45,0.3);
    font-family: 'Poppins', sans-serif;
}
</style>
""", unsafe_allow_html=True)

# -------------------- TITLE --------------------
# The '✨' emoji will now be a golden color due to the gradient applied to h1.app-title
st.markdown("""
<h1 class='app-title'>✨ Image Processing Studio</h1>
<h2 class='app-subtitle'>🎨 Clean • Aesthetic • Easy-to-use 🖌️</h2>
""", unsafe_allow_html=True)

# -------------------- SIDE MENU --------------------
st.sidebar.markdown('<h2 class="sidebar-title">📌 Image Processing Menu</h2>', unsafe_allow_html=True)

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
    st.markdown('<div class="footer">Powered by Streamlit and OpenCV</div>', unsafe_allow_html=True)
    st.stop()

# --- Image Processing Setup ---
image = Image.open(uploaded_file)
# Convert PIL Image to OpenCV (BGR)
img_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
# Convert to grayscale for some operations
gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
w, h = image.size

# -------------------- DOWNLOAD FUNCTION --------------------
def download_image(img, filename):
    buf = BytesIO()
    img.save(buf, format="PNG")
    st.download_button("📥 Download Image", buf.getvalue(), file_name=filename)

# -------------------- HOME --------------------
if menu == "home":
    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.markdown("---")
    st.markdown("### 🔧 Features You Can Explore:")
    st.markdown("""
    <ul style="list-style-type: '👉'; padding-left: 20px; font-weight: 500;">
        <li>**Grayscale:** Convert to classic black and white.</li>
        <li>**Rotate:** Spin the image 90°, 180°, or 270°.</li>
        <li>**Mirror:** Flip the image horizontally.</li>
        <li>**Contours:** Outline the shapes and objects in the image.</li>
        <li>**50-50 Split:** Cut the image perfectly in half (vertical/horizontal).</li>
        <li>**Custom Split:** Slice the image vertically by a custom percentage.</li>
        <li>**4×4 Grid:** Break the image into 16 equal tiles.</li>
    </ul>
    """, unsafe_allow_html=True)
    st.markdown("---")
    st.markdown('<div class="footer">Ready to process! Select an option from the sidebar.</div>', unsafe_allow_html=True)

# -------------------- IMAGE PROPERTIES --------------------
elif menu == "props":
    st.title("📏 Image Properties")
    st.markdown("---")
    col1, col2 = st.columns([1, 1.5]) 
    with col1:
        st.image(image, caption="Uploaded Image", use_column_width=True)
    with col2:
        st.markdown("### 📊 Image Details")
        st.markdown(f"**🖼 Size (Width × Height):** <span style='font-weight: 700; color: #A0522D;'>{w} × {h}</span> pixels", unsafe_allow_html=True)
        st.markdown(f"**🎯 PIL Mode:** <span style='font-weight: 700; color: #A0522D;'>{image.mode}</span> (e.g., RGB, L)", unsafe_allow_html=True)
        st.markdown(f"**🔍 OpenCV Shape:** <span style='font-weight: 700; color: #A0522D;'>{np.array(img_cv).shape}</span> (Height, Width, Channels)", unsafe_allow_html=True)
    st.markdown("---")

# -------------------- GRAYSCALE --------------------
elif menu == "gray":
    st.title("⚫ Grayscale Image")
    st.markdown("---")
    st.info("Grayscale conversion removes color information, leaving only luminance.")
    gray_img = Image.fromarray(gray)
    st.image(gray_img, caption="Grayscale Output", use_column_width=True)
    download_image(gray_img, "grayscale.png")
    st.markdown("---")

# -------------------- ROTATE --------------------
elif menu == "rotate":
    st.title("🔄 Rotate Image")
    st.markdown("---")
    angle = st.radio("Choose rotation:", [90, 180, 270], horizontal=True)
    rotated = image.rotate(angle, expand=True)
    st.image(rotated, caption=f"Rotated {angle}°", use_column_width=True)
    download_image(rotated, f"rotated_{angle}.png")
    st.markdown("---")

# -------------------- MIRROR --------------------
elif menu == "mirror":
    st.title("🪞 Mirror Image")
    st.markdown("---")
    st.info("This performs a horizontal flip (left-to-right mirror).")
    mirrored = image.transpose(Image.FLIP_LEFT_RIGHT)
    st.image(mirrored, caption="Horizontally Mirrored Image", use_column_width=True)
    download_image(mirrored, "mirrored.png")
    st.markdown("---")

# -------------------- CONTOURS --------------------
elif menu == "contours":
    st.title("🟢 Contour Detection")
    st.markdown("---")
    st.info("Contours are continuous curves used for object shape analysis.")
    edges = cv2.Canny(gray, 100, 200)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contoured = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(contoured, contours, -1, (128,255,128), 2)
    contoured_img = Image.fromarray(cv2.cvtColor(contoured, cv2.COLOR_BGR2RGB))
    
    st.write(f"✨ **Total Contours Found:** <span style='font-weight: 700; color: #A0522D;'>{len(contours)}</span>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    col1.image(edges, caption="Edge Detection (Canny)", use_column_width=True)
    col2.image(contoured_img, caption="Contours Drawn", use_column_width=True)
    download_image(contoured_img, "contours.png")
    st.markdown("---")

# -------------------- 50/50 SPLIT --------------------
elif menu == "cut":
    st.title("✂ Vertical & Horizontal 50/50 Cut")
    st.markdown("---")
    left = image.crop((0, 0, w//2, h))
    right = image.crop((w//2, 0, w, h))
    top = image.crop((0, 0, w, h//2))
    bottom = image.crop((0, h//2, w, h))
    
    st.markdown("### 📌 Vertical Split (Left / Right)")
    col1, col2 = st.columns(2)
    col1.image(left, caption="Left Half (50%)", use_column_width=True)
    col2.image(right, caption="Right Half (50%)", use_column_width=True)
    
    st.markdown("### 📌 Horizontal Split (Top / Bottom)")
    col3, col4 = st.columns(2)
    col3.image(top, caption="Top Half (50%)", use_column_width=True)
    col4.image(bottom, caption="Bottom Half (50%)", use_column_width=True)
    st.markdown("---")

# -------------------- CUSTOM PERCENT SPLIT --------------------
elif menu == "custom":
    st.title("📐 Custom Percentage Vertical Cut")
    st.markdown("---")
    percent = st.slider("Select left side percentage for vertical split:", 10, 90, 50, 5) 
    cut_x = int((percent / 100) * w)
    p1 = image.crop((0, 0, cut_x, h))
    p2 = image.crop((cut_x, 0, w, h))
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"### 🔸 Left: {percent}%")
        st.image(p1, caption=f"Left {percent}% Portion", use_column_width=True)
    with col2:
        st.markdown(f"### 🔹 Right: {100 - percent}%")
        st.image(p2, caption=f"Right {100 - percent}% Portion", use_column_width=True)
    st.markdown("---")


# -------------------- 4×4 GRID --------------------
elif menu == "grid":
    st.title("🔳 4×4 Grid Split (16 Tiles)")
    st.markdown("---")
    grid_rows = 4
    grid_cols = 4
    tile_w = w // grid_cols
    tile_h = h // grid_rows
    tiles = []
    
    # Calculate and crop tiles
    for r in range(grid_rows):
        for c in range(grid_cols):
            left = c * tile_w
            upper = r * tile_h
            right = (c+1)*tile_w if c < grid_cols-1 else w
            lower = (r+1)*tile_h if r < grid_rows-1 else h
            tiles.append(image.crop((left, upper, right, lower)))
            
    st.write(f"📦 **Generated <span style='font-weight: 700; color: #A0522D;'>{len(tiles)}</span> tiles:**", unsafe_allow_html=True)
    
    # Display tiles in a 4-column layout
    cols = st.columns(4)
    for i, tile in enumerate(tiles):
        cols[i % 4].image(tile, caption=f"Tile {i+1}", use_column_width=True)
    st.markdown("---")

# Add a subtle footer at the end of every active page
if uploaded_file is not None:
    st.markdown('<div class="footer">Thank you for using the Image Processing Studio!</div>', unsafe_allow_html=True)
