# Copyright (c) johnsons-ds
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# Load packages
import os
import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from streamlit_folium import folium_static
import geopandas as gpd
from dotenv import load_dotenv
from shapely.geometry import Point
from streamlit_extras.colored_header import colored_header

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variable
google_maps_api_key = os.getenv("GOOGLE_MAPS_API_KEY")

# Set page configuration
st.set_page_config(
    page_title="ACT Road Signs Data",
    page_icon="🚙",
    layout="centered",
    initial_sidebar_state="auto"
)

# Displaying a colored header with specified parameters
colored_header(
    label="ACT Road Signs 🪧 Data 📊",
    description="~ Developed by johnsons-ds",
    color_name="violet-70",
)



# Load the road signs open data (replace 'your_data.csv' with the actual file path or URL)
data = pd.read_csv('https://www.data.act.gov.au/resource/5x84-xpn7.csv')


# Create a GeoDataFrame from the DataFrame
geometry = [Point(xy) for xy in zip(data.longitude, data.latitude)]
gdf = gpd.GeoDataFrame(data, geometry=geometry)

# Set up Streamlit app
st.title('Parking Signs in the ACT')
st.sidebar.header('Filter Options')

# Filter by sign purpose
selected_purpose = st.sidebar.selectbox('Select Sign Purpose', data['sign_purpose'].unique(), index=4)
st.write(selected_purpose)

# Filter by sign text
#selected_text = st.sidebar.text_input('Enter Sign Text', '')
selected_texts = st.sidebar.multiselect('Select Sign Text',  data[(data['sign_purpose'] == selected_purpose)]['sign_text'].unique(), default='NO PARKING')

# Filter data based on selected purpose and text
filtered_data = data[(data['sign_purpose'] == selected_purpose) & (data['sign_text'].isin(selected_texts))]

# Create a folium map centered around ACT
act_map = folium.Map(location=[-35.282001, 149.128998], zoom_start=11)

# Add markers for each data point
for index, row in filtered_data.iterrows():
    # Include 'suburb' and 'location_description' in the popup content
    popup_content = f"{row['sign_text']}<br>Suburb: {row['suburb']}<br>Location Description: {row['location_description']}"
    folium.Marker([row['latitude'], row['longitude']], popup=popup_content).add_to(act_map)

# Render the folium map using streamlit
folium_static(act_map)

st.sidebar.markdown(
    """
    
"""
)
st.sidebar.markdown(
    """
    
"""
)
st.sidebar.markdown(
    """
    
"""
)
st.sidebar.markdown(
    """
    Developed by johnsons-ds [![GitHub](https://img.shields.io/badge/GitHub-Profile-blue?style=social&logo=github)](https://github.com/johnsons-ds)

"""
)

# Display Google Map using iframe (Coming Soon!)
#google_map_url = f"https://www.google.com/maps/embed/v1/place?key={google_maps_api_key}&q=-35.282001,149.128998&zoom=11"
#st.subheader("Google Map View")


#st.components.v1.html(f'<iframe width="800" height="600" frameborder="0" style="border:0" src="{google_map_url}" allowfullscreen></iframe>', height=600)