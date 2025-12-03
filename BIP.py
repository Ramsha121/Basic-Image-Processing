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

# -------------------- CUSTOM PAGE THEME 🎨 --------------------
st.markdown("""
    <style>
        .main { background-color: #f4f7fb; }
        .stButton>button {
            background-color:#ff4b4b;
            color:white;
            border-radius:10px;
            padding:8px 20px;
        }
        .stRadio>div { 
            background:white; 
            padding:10px; 
            border-radius:10px; 
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

# -------------------- HELPER: DOWNLOAD BUTTON --------------------
def download_image(img, filename):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_img = buf.getvalue()
    st.download_button("📥 Download", data=byte_img, file_name=filename, mime="image/png")


# ====================== IF NO IMAGE ======================
if not uploaded_file:
    st.info("⬅️ Upload an image from the **left sidebar** to begin.")
    st.stop()

# Load image
image = Image.open(uploaded_file)
img_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
w, h = image.size


# ====================== HOME ======================
if menu == "🏠 Home":
    st.title("🎨 Image Processing App (OpenCV + PIL)")
    st.subheader("✨ Made simple, colorful & beginner-friendly ✨")
    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.markdown("""
    ### 🔧 What You Can Do:
    - Convert to **Grayscale**
    - **Rotate** in 90° / 180° / 270°
    - Create **Mirror image**
    - Detect **Contours**
    - Split image **50-50 Vertical/Horizontal**
    - Make **Custom % Cut**
    - Generate **4×4 Grid Tiles**
    
    👉 Use the **menu on the left** to explore each feature!
    """)


# ====================== IMAGE PROPERTIES ======================
elif menu == "📏 Image Properties":
    st.title("📏 Image Properties")

    col1, col2 = st.columns(2)
    with col1:
        st.image(image, caption="Original Image", use_column_width=True)

    with col2:
        st.write(f"🖼 **Size (W × H):** `{w} × {h}`")
        st.write(f"🎯 **Mode:** `{image.mode}`")
        st.write(f"🔍 **Shape:** `{np.array(img_cv).shape}`")



# ====================== GRAYSCALE ======================
elif menu == "⚫ Grayscale":
    st.title("⚫ Grayscale Image")

    gray_img = Image.fromarray(gray)
    st.image(gray_img, caption="Grayscale", use_column_width=True)
    download_image(gray_img, "grayscale.png")



# ====================== ROTATE ======================
elif menu == "🔄 Rotate Image":
    st.title("🔄 Rotate Image")

    angle = st.radio("Choose rotation angle:", [90, 180, 270], horizontal=True)
    rotated = image.rotate(angle, expand=True)

    st.image(rotated, caption=f"Rotated {angle}°", use_column_width=True)
    download_image(rotated, f"rotated_{angle}.png")



# ====================== MIRROR ======================
elif menu == "🪞 Mirror Image":
    st.title("🪞 Mirror Image")

    mirrored = image.transpose(Image.FLIP_LEFT_RIGHT)
    st.image(mirrored, caption="Mirrored Image", use_column_width=True)
    download_image(mirrored, "mirrored.png")



# ====================== CONTOURS ======================
elif menu == "🟢 Contours":
    st.title("🟢 Contour Detection")

    edges = cv2.Canny(gray, 100, 200)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    st.write(f"✨ **Contours Detected:** `{len(contours)}` shapes")

    contoured = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(contoured, contours, -1, (0,255,0), 2)
    contoured_img = Image.fromarray(cv2.cvtColor(contoured, cv2.COLOR_BGR2RGB))

    col1, col2 = st.columns(2)
    col1.image(edges, caption="Canny Edges", use_column_width=True)
    col2.image(contoured_img, caption="Contour Output", use_column_width=True)

    download_image(contoured_img, "contours.png")



# ====================== 50/50 CUT ======================
elif menu == "✂ Vertical / Horizontal Cut":
    st.title("✂ 50-50 Image Split")

    left = image.crop((0, 0, w//2, h))
    right = image.crop((w//2, 0, w, h))
    top = image.crop((0, 0, w, h//2))
    bottom = image.crop((0, h//2, w, h))

    st.subheader("📌 Vertical (Left / Right)")
    c1, c2 = st.columns(2)
    c1.image(left, caption="Left Half")
    c2.image(right, caption="Right Half")

    st.subheader("📌 Horizontal (Top / Bottom)")
    c3, c4 = st.columns(2)
    c3.image(top, caption="Top Half")
    c4.image(bottom, caption="Bottom Half")



# ====================== CUSTOM CUT ======================
elif menu == "📐 Custom Percentage Cut":
    st.title("📐 Custom Percentage Cut")

    percent = st.slider("Select split % for left part:", 10, 90, 80)
    cut_x = int((percent/100) * w)

    p1 = image.crop((0, 0, cut_x, h))
    p2 = image.crop((cut_x, 0, w, h))

    st.write(f"🔸 **Left: {percent}%**")
    st.image(p1)

    st.write(f"🔹 **Right: {100-percent}%**")
    st.image(p2)



# ====================== 4×4 GRID ======================
elif menu == "🔳 4×4 Grid Split":
    st.title("🔳 4 × 4 Grid Split")

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

    for i, tile in enumerate(tiles):
        st.image(tile, caption=f"Tile {i+1}", width=200)
