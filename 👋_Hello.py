import streamlit as st
import pandas as pd
import numpy as np
import cv2
import tensorflow as tf
from tensorflow.keras.models import load_model

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
    layout="wide"

)
#load the model
@st.cache_resource
def load_model_(model_path):
    model =load_model(model_path)
    return model

#Prepare the image uploaded 
def prepare_img(filepath):
    img_ = cv2.imread(filepath)
    resize = tf.image.resize(img_, (224,224))
    return np.expand_dims(resize/255, 0)

labels = ["FEMALE","MALE"]
labels_dict={1:'Male',0:'Female'}
color_dict={0:(0,0,255),1:(0,255,0)}
st.title("Gender Classification")
st.header("Hi their ! You can detect the gender of a given image")
st.sidebar.title("Paramaters")

st.sidebar.header("You can adjust this paramatres")

model_chose  = st.sidebar.selectbox("Models",["model_1","model_2","model_3"])
model = load_model_(model_chose+".h5")
image_streamlit  = st.file_uploader("Upload your image",type=["jpg","png","jpeg"])
col1, col2= st.columns((1,1),gap="medium")

if image_streamlit != None:
    with col1:
        st.image(image_streamlit)
    with open("files/"+image_streamlit.name,mode = "wb") as f: 
        f.write(image_streamlit.getbuffer())      
    st.success("Saved File")
    image = cv2.imread("files/"+image_streamlit.name)
    #Setup the file path and the algo path
    alg = "haarcascade_frontalface_default.xml"
    haar_cascade = cv2.CascadeClassifier(alg)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # loop through all the faces in the image and get the crop face of each person then predict it take the crop face then put the predict label
    for i,(x, y, w, h) in enumerate(faces):
        face_crop = image[y:y+h, x:x+w]
        pict_name = 'cut_face.jpg'
        cv2.imwrite(pict_name, face_crop)
        pred = model.predict(prepare_img(pict_name))
        class_ = int(pred.round()[:,0])
        cv2.rectangle(image, (x, y), (x+w, y+h), color_dict[class_], 2)
        cv2.rectangle(image, (x, y - 24), (x + w, y), (0,0,0) ,-1)
        cv2.putText(image, f'{labels[class_]}', (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.8 ,color_dict[class_], 1)
    cv2.imwrite("imageDetect.jpg", image)
    with col2:
        st.image("imageDetect.jpg")




# TO DO: ADD camera future