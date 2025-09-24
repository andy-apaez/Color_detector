import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import streamlit as st
from io import BytesIO

st.title("Andy's dominant color detector")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

def get_dominant_colors(img, k=5):
    # Convert to RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Reshape
    pixels = img.reshape((-1, 3))

    # KMeans clustering
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(pixels)

    colors = kmeans.cluster_centers_.astype(int)
    labels = kmeans.labels_
    counts = np.bincount(labels)

    sorted_idx = np.argsort(-counts)
    colors = colors[sorted_idx]
    counts = counts[sorted_idx]
    percentages = counts / counts.sum()

    return list(zip([tuple(c) for c in colors], percentages))

if uploaded_file is not None:
    # Read uploaded image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)

    st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), caption="Uploaded Image", use_container_width=True)


    st.subheader("Top Colors")
    dominant = get_dominant_colors(img, k=5)

    # Show colors as swatches
    cols = st.columns(len(dominant))
    for i, (color, pct) in enumerate(dominant):
        rgb_str = f"RGB: {color} | {pct*100:.1f}%"
        hex_color = '#%02x%02x%02x' % color
        with cols[i]:
            st.markdown(
                f"<div style='background-color:{hex_color}; width:100px; height:100px; border-radius:10px;'></div>",
                unsafe_allow_html=True
            )
            st.write(rgb_str)
