import streamlit as st
from PIL import Image
# run in terminal streamlit run bonus/bonus1.py to run the App

with st.expander("Start Camera"):
    # Start the camera in the web
    camera_image = st.camera_input("Camera")

if camera_image:
    # piece of code that create a PIL image instance
    img = Image.open(camera_image)  # camera_image used as arg for the PIL image(Will give us a PIL image type)

    # Converts the image to grayscale
    out = st.image.point(lambda i: i * 20)  # "L"(notion) one of the algorithms that converts to grayscale
    gray_img = img.convert("L")
    # display the grayscale on the webpage
    st.image(out)
    st.image(gray_img)


# gray_img = img.convert("L")
# multiply each pixel by 20
# out = im.point(lambda i: i * 20)

