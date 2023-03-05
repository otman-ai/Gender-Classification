import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
st.set_page_config(page_title="Models inshight", page_icon="📈",layout="wide")

@st.cache_data
def load_model_insight_(df):
    data = pd.read_csv(df)
    return data

st.title("Models Insight")

model_data = load_model_insight_("pages/model_performance.csv")
model_data

col1,col2,col3,col4 = st.columns((1,1,1,1))

with col1:
    y_name = "ValAccuracy"
    fig = px.histogram(model_data, x='models', y=y_name, height=300,title=f"Models by {y_name}") 
    st.plotly_chart(fig,use_container_width=True)

with col2:
    y_name = "BinaryAccuracy"
    fig1 = px.histogram(model_data, x='models', y=y_name, height=300,title=f"Models by {y_name}") 
    st.plotly_chart(fig1, use_container_width=True)

with col3:
    y_name="Recall"
    fig3 = px.histogram(model_data, x='models', y=y_name, height=300,title=f"Models by {y_name}") 
    st.plotly_chart(fig3, use_container_width=True)

with col4:
    y_name = "Precision"
    fig2 = px.histogram(model_data, x='models', y=y_name, height=300,title=f"Models by {y_name}") 
    st.plotly_chart(fig2, use_container_width=True)


