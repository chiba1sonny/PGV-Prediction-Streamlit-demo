import xgboost as xgb
import streamlit as st
import pandas as pd
from pathlib import Path


model = xgb.XGBRegressor()
model.load_model('model.json')
@st.cache

def predict(Mw, Distance, Depth):
    prediction = model.predict(pd.DataFrame([[Mw, Distance, Depth]], columns=['Mw', 'Distance', 'Depth']))
    return prediction

def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()
intro_markdown = read_markdown_file("introduction.md")
st.markdown(intro_markdown, unsafe_allow_html=True)

st.write('Mw, Distance, Depthを入力してください')

Mw = st.sidebar.number_input('Mw:', min_value=1, max_value=12, value=6)
Distance = st.sidebar.number_input('Distance:', min_value=1, max_value=500, value=50)
Depth = st.sidebar.number_input('Depth:', min_value=1, max_value=150, value=10)

if st.button('log(pgv)='):
    logpgv = predict(Mw, Distance, Depth)
    st.success(f'{logpgv[0]:.2f}')

if st.button('pgv='):
    logpgv = predict(Mw, Distance, Depth)
    pgv = 10**logpgv
    st.success(f'{pgv[0]:.2f}')
