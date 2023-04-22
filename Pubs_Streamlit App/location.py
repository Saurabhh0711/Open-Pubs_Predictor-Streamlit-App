import streamlit as st
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static
st.set_page_config(layout="wide")



df = pd.read_csv('new_pubs_data.csv')

st.title(":green[Locations Of Pubs:-]")


location_type = st.selectbox(
    "Select the location type:",
    ('Postal Code', 'Local Authority'))

if location_type == 'Postal Code':
    location_options = df['postcode'].unique()
    location = st.selectbox("Select the Postal Code:", location_options)
    filtered_df = df[df['postcode'] == location]
elif location_type == 'Local Authority':
    location_options = df['local_authority'].unique()
    location = st.selectbox("Select the Local Authority:", location_options)
    filtered_df = df[df['local_authority'] == location]

if not filtered_df.empty:
    st.write("Number of Pubs in the area:", filtered_df.shape[0])


    pub_map = folium.Map(location=[filtered_df['latitude'].mean(), filtered_df['longitude'].mean()], zoom_start=12)

    mc = MarkerCluster()
    for row in filtered_df.iterrows():
        mc.add_child(folium.Marker(location=[row[1]['latitude'], row[1]['longitude']], popup=row[1]['name']))
    pub_map.add_child(mc)

    # display the map
    folium_static(pub_map)
else:
    st.write("No Pubs are in the area.")