import streamlit as st
import cv2
from PIL import Image
import numpy as np
import os
try:
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
except Exception:
    st.write("Error loading cascade classifiers")

def detect(image):
    image = np.array(image.convert('RGB'))
    faces = face_cascade.detectMultiScale(image=image, scaleFactor=1.3, minNeighbors=5)
    name="Unknown"
    for (x, y, w, h) in faces:
        y1,x2,y2,x1=faceloc
        y1,x2,y2,x1=y1*4,x2*4,y2*4,x1*4
        cv2.rectangle(img=image, pt1=(x, y), pt2=(x + w, y + h), color=(255, 0, 0), thickness=2)       
        cv2.putText(img=image,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
    return image, faces
def about():
	st.write(
		'''It is just an demo page for showing the face Detection using Haar cascade Classifiers
        and for making this webpage we are taking help from bootstrap for making this webpage and it is uploaded on heroku  
Read more :point_right: https://docs.opencv.org/2.4/modules/objdetect/doc/cascade_classification.html
https://sites.google.com/site/5kk73gpu2012/assignment/viola-jones-face-detection#TOC-Image-Pyramid
		''')
def main():
    st.title("Face Detection App :smile: ")
    st.write("**Using the Haar cascade Classifiers**")
    activities = ["Home", "About"]
    choice = st.sidebar.selectbox("Select the Option", activities)
    if choice == "Home":
    	st.write("Go to the About section from the sidebar to know more about this project.")
        # You can specify more file types below if you want
    	image_file = st.file_uploader("Upload image", type=['jpeg', 'png', 'jpg', 'webp'])
    	if image_file is not None:
    		image = Image.open(image_file)
    		if st.button("Continue"):
                result_img, result_faces = detect(image=image)
    			st.image(result_img, use_column_width = True)
    			st.success("Found {} faces\n".format(len(result_faces)))
    elif choice == "About":
    	about()
if __name__ == "__main__":
    main()
