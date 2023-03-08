import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from plotly import graph_objs as go

st.set_page_config(page_title="Models inshight", page_icon="📈",layout="wide")

def load_model_insight_(df):
    data = pd.read_csv(df)
    return data

st.title("Models Insight")

model_data_acc = load_model_insight_("history_files/history_1.csv")
history_df_1 = pd.read_csv("history_files/history_1.csv")
history_df_2 = pd.read_csv("history_files/history_2.csv")
history_df_3 = pd.read_csv("history_files/history_3.csv")

model_1_acc = pd.read_csv("Acc files/model_1_acc.csv")
model_2_acc = pd.read_csv("Acc files/model_2_acc.csv")
model_3_acc = pd.read_csv("Acc files/model_3_acc.csv")
epochs = range(len(history_df_1["val_accuracy"]))

col1,col2 = st.columns((1,1))
with col1:
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=history_df_3.index, y=history_df_1["val_accuracy"], name="model_1"))
    fig.add_trace(go.Scatter(x=history_df_3.index, y=history_df_2["val_accuracy"], name="model_2"))
    fig.add_trace(go.Scatter(x=history_df_3.index, y=history_df_3["val_accuracy"], name="model_3"))
    fig.layout.update(title="models performance in the training data (Validation Accuracy)",xaxis_rangeslider_visible=True)
    st.plotly_chart(fig,use_container_width=True)
with col2:
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(x=history_df_3.index, y=history_df_1["val_loss"], name="model_1"))
    fig1.add_trace(go.Scatter(x=history_df_3.index, y=history_df_2["val_loss"], name="model_2"))
    fig1.add_trace(go.Scatter(x=history_df_3.index, y=history_df_3["val_loss"], name="model_3"))
    fig1.layout.update(title="models performance in the training data Validation Losses",xaxis_rangeslider_visible=True)
    st.plotly_chart(fig1,use_container_width=True)

colA,colB,colC = st.columns((1,1,1),gap="large")
with colA:
    st.markdown("<h4>Model 1</h4>",unsafe_allow_html=True)
    model_1_acc
    st.markdown("<h5>Model 1 Matrix </h5>",unsafe_allow_html=True)
    fig_ = px.bar(model_1_acc.loc[model_1_acc["matrix"] != "support"],y=["female","male"],x="matrix",barmode="group",width=400,height=350)
    st.plotly_chart(fig_,use_container_width=False)

with colB :
    st.markdown("<h4>Model 2</h4>",unsafe_allow_html=True)
    model_2_acc
    st.markdown("<h5>Model 2 Matrix </h5>",unsafe_allow_html=True)
    fig_1 = px.bar(model_2_acc.loc[model_2_acc["matrix"] != "support"],y=["female","male"],x="matrix",barmode="group",width=400,height=350)
    st.plotly_chart(fig_1,use_container_width=False)

with colC:
    st.markdown("<h4>Model 3</h4>",unsafe_allow_html=True)
    model_3_acc
    st.markdown("<h5>Model 3 Matrix </h5>",unsafe_allow_html=True)
    fig_2 = px.bar(model_3_acc.loc[model_3_acc["matrix"] != "support"],y=["female","male"],x="matrix",barmode="group",width=400,height=350)
    st.plotly_chart(fig_2,use_container_width=False)
