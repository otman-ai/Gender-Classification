import streamlit as st
st.set_page_config(page_title="Model building Processe",layout="wide",
page_icon="🌍")
st.title("Gender Classification")

st.info("[Gender classification](https://link.springer.com/chapter/10.1007/978-3-642-30157-5_6#:~:text=A%20gender%20classification%20system%20uses,and%20smart%20human%2Dcomputer%20interface.) system uses face of a person from a given image to tell the gender (male/female) of the given person. A successful gender classification approach can boost the performance of many other applications including face recognition and smart human-computer interface.basically gender classification is one of computer vision problem.")
st.info("**What is computer vision?**:\n well according to [wikipedia](https://en.wikipedia.org/wiki/Computer_vision) Computer vision tasks include methods for acquiring, processing, analyzing and understanding digital images, and extraction of high-dimensional data from the real world in order to produce numerical or symbolic information")

st.markdown("<h2>Model Building Processe</h2>",unsafe_allow_html=True)

st.write("Build ML model is one of the most hard and fun things to do . I went throught several steps to make this gender classification model .")
st.warning("This Steps can fit to any ML project.")

st.markdown("<h4>1.Data Collection</h2>",unsafe_allow_html=True)
st.write("Using pre-collected data, by way of datasets from [Kaggle](https://www.kaggle.com/datasets/cashutosh/gender-classification-dataset).The data set is of cropped images of male and female . It is split into training and validation directory. Training contains ~23,000 images of each class and validation directory contains ~5,500 images of each class.")

st.markdown("<h4>2.Build a series of models </h2>",unsafe_allow_html=True)
st.write("Ml is all about experiment ,Model tweaking, regularization, and hyperparameter tuning this is where we iteratively go from a ~good enough~ model to our best effort.In this step I have build three differents models **(differnets layers structure , number and the change on some prametres)**")

st.markdown("<h4>3.Evaluate all the models performance</h2>",unsafe_allow_html=True)
st.write("In each model we evaluate the model performance to see how it behave against unseen data,we Uses some metric like *Binary Accuracy* , *Recall*, *Precision*")

st.markdown("<h4>4.Download the models on our local directory for Deployment uses <h4>",unsafe_allow_html=True)
st.write("Save the models on our local directory")

st.markdown("<h4>5.Test the model on random Image from the web</h4>",unsafe_allow_html=True)
st.write("Pick up any random image from the web and we test to see on real world the performance of our models")

st.markdown("<h4>6.Deploy our model</h4>",unsafe_allow_html=True)
st.write("We deploy the models using library for data science deployment in python called [Streamlit](https://streamlit.io/),it makes easy to build and deploy web app ")
# TO DO