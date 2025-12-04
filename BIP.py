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
