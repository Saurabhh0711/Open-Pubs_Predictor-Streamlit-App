import streamlit as st
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from PIL import Image
import base64
st.set_page_config(layout="wide")



df = pd.read_csv('new_pubs_data.csv')

st.title(":red[----------Pubs Dataset Analysis----------------- ]")


st.markdown("## :green[Dataset Info:-]")

st.markdown("###### Top Five Rows of Dataset")
st.write(df.head())

st.markdown("###### Bottom Five Rows of Dataset")
st.write(df.tail())

st.markdown("###### Total Numbers of Rows and Columns")
st.write("Total number of Pubs:", df.shape[0])
st.write("Total number of columns:", df.shape[1])


st.markdown("###### Null Values")
st.write(df.isnull().sum())

st.markdown("###### Duplicated Values")
st.write(df.duplicated().sum())
