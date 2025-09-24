**Dominant Color Detector**

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
//Notes//

The number of dominant colors can be adjusted by changing the k parameter in the get_dominant_colors function.

This app works best for images with a moderate number of distinct colors.

use_container_width=True is used to make the uploaded image responsive.
