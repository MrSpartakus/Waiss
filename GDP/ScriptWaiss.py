#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import libraries

import folium
from folium.features import CustomIcon
import json
import pandas as pd
import geopandas as gpd


# In[2]:


#Read geojson file with geopandas

yugo = gpd.read_file('/Users/agustincosovschi/Trabajo/ProduccionPropia/Artículos/WaissEspacial/Visuals/Selection/GDP/yugo.geojson')


# In[3]:


#Explore geojson 

print(yugo)


# In[5]:


#Create DF with data for Chloropleth

republics = ['Bosnia and Herzegovina', 'Slovenia', 'Serbia', 'Vojvodina', 'Kosovo', 'Montenegro', 'Macedonia', 'Croatia']

gdp_per_capita = [83, 165, 91, 94, 43, 77, 68, 122]

df = pd.DataFrame(list(zip(republics, gdp_per_capita)), columns=['Republic/region', 'GDP per capita (index)'])


# In[6]:


#Explore DF
print(df)


# In[41]:


#Create map with Folium

m = folium.Map(location=[44, 19], tiles= 'cartodbpositron', zoom_start=6)



# In[42]:


#Choropleth

folium.Choropleth(
    geo_data=yugo,
    name='Countries by GDP',
    data=df,
    columns=['Republic/region', 'GDP per capita (index)'],
    key_on='feature.properties.sovereignt',
    fill_color='Greys',
    fill_opacity=1,
    line_opacity=1,
    legend_name='GDP index (1953). Yugoslavia=100.', 
    reset=True
).add_to(m)

folium.LayerControl().add_to(m)

m


# In[9]:


#Create new DF from CSV for points

df_waiss = pd.read_csv('/Users/agustincosovschi/Trabajo/ProduccionPropia/Artículos/WaissEspacial/Visuals/Selection/GDP/Localities_QGIS - Hoja 1.csv')


# In[10]:


lats = []

for lat in df_waiss['Latitude']:
    lats.append(lat)

print(lats)


# In[11]:


longs = []

for lng in df_waiss['Longitude']:
    longs.append(lng)

print(longs)


# In[12]:


locs = []

for loc in df_waiss['Place']:
    locs.append(loc)

print(locs)


# In[13]:


locations = [list(a) for a in zip(lats, longs, locs)]


# In[14]:


print(locations)


# In[45]:


#Introduce points in map M

for location in locations:    
    folium.Marker([location[0],location[1]], tooltip=location[2],
                  icon=folium.Icon(color='darkred', icon='user')
                 
                 ).add_to(m)
    
    
m


# In[28]:


#Save map

m.save('/Users/agustincosovschi/Trabajo/ProduccionPropia/Artículos/WaissEspacial/Visuals/Selection/GDP/WaissXGDP_User.html')


# In[ ]:





# In[ ]:




