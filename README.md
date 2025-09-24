🎨**Dominant Color Detector**
![Python](https://img.shields.io/badge/Python-3.11-blue)
![License](https://img.shields.io/badge/License-MIT-green)

A Python web app that detects the dominant colors in an uploaded image using KMeans clustering. Users can upload an image via their browser, view the image, and see a palette of the most prominent colors along with their RGB values and percentages.

---
**DEMO**

![Uploading ezgif.com-video-to-gif-converter (4).gif…]()

---
**Features**

- Upload JPG/PNG images via a browser interface.

- Detect top dominant colors in the image.

- Display colors as visual swatches with RGB values and percentage coverage.

- Lightweight and easy to run locally using Streamlit.

---
**Tech Stack**

Python 3.x

Streamlit
 – for the browser interface

OpenCV
 – for image processing

scikit-learn
 – for KMeans clustering

Matplotlib
 – for optional plotting

---
**Python Dependencies**
streamlit==1.27.0        # For browser-based UI
opencv-python==4.8.1.78  # For image processing
scikit-learn==1.3.1      # For KMeans clustering
matplotlib==3.8.0        # Optional for plotting colors (used in development)
numpy==1.26.0            # For numerical operations on arrays

---
>Notes

The number of dominant colors can be adjusted by changing the k parameter in the get_dominant_colors function.

This app works best for images with a moderate number of distinct colors.

use_container_width=True is used to make the uploaded image responsive.
