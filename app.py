#!/usr/bin/env python
# coding: utf-8
# In[ ]:


# In[21]:

import pandas as pd
import geopandas as gpd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderUnavailable
import streamlit as st
import folium


# In[22]:


info_df= pd.read_excel('data.xlsx')


# In[23]:


info_df


# In[34]:


def create_ticker_map(info_df):
    us_map = folium.Map(location=[37.0902, -95.7129], zoom_start=4)
    
    district_colors = {}  # Dictionary to store colors for each district

    for index, row in info_df.iterrows():
        latitude = row['Latitude']
        longitude = row['Longitude']
        ticker = row['Ticker']
        headquarters = row['Headquarters']
        district = row['District']
        
        if pd.notnull(latitude) and pd.notnull(longitude):
            if district != 'N/A':
                if district not in district_colors:
                    district_colors[district] = 'blue' if len(district_colors) % 2 == 0 else 'green'
                
                color = district_colors[district]
            else:
                color = 'red'

            folium.Marker(
                location=[latitude, longitude],
                popup=f"{ticker} - {headquarters}<br>District: {district}",
                icon=folium.Icon(color=color, icon='times')
            ).add_to(us_map)
    
    return us_map


# In[49]:


def create_us_map():
    us_map = folium.Map(location=[37.0902, -95.7129], zoom_start=4)
    # Add markers, layers, etc. to the map
    return us_map


# In[50]:


def main():
    st.title("Ticker Headquarters Map")
    st.write("Displaying ticker headquarters on the map based on Federal Reserve districts.")
    st.write("Blue markers indicate known districts. Red markers indicate unknown districts.")

    # Read the saved HTML map
    us_map = create_us_map()


    # Display the map using Streamlit
    st.write(us_map._repr_html_(), unsafe_allow_html=True)

if __name__ == "__main__":
    main()


# In[44]:


# 다운로드한 파일을 로컬 환경으로 가져오기
from google.colab import files
files.download('plot.py')


# In[ ]:


# Streamlit app
st.title("Ticker Headquarters Map")
st.write("Displaying ticker headquarters on the map based on Federal Reserve districts.")
st.write("Blue markers indicate known districts. Red markers indicate unknown districts.")

# Display the map using Streamlit
st.markdown(us_map._repr_html_(), unsafe_allow_html=True)


# In[ ]:


import streamlit as st

def main():
    st.title("Ticker Map")

    # Load the saved HTML map
    with open("ticker_map.html", "r") as f:
        map_html = f.read()

    # Display the map using Streamlit
    st.components.v1.html(map_html, width=800, height=600)

if __name__ == "__main__":
    main()

