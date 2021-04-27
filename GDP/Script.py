#!/usr/bin/env python
# coding: utf-8

# In[177]:


#Import libraries

import folium
from folium.features import CustomIcon
import json
import pandas as pd
import geopandas as gpd


# In[178]:


#Read geojson file with geopandas

yugo = gpd.read_file('/Users/agustincosovschi/Trabajo/ProduccionPropia/Artículos/WaissEspacial/Visuals/Selection/GDP/yugo.geojson')


# In[179]:


#Explore geojson 

print(yugo.head(25))


# In[180]:


#Create DF with data for Chloropleth

republics = ['Bosnia and Herzegovina', 'Slovenia', 'Serbia', 'Vojvodina', 'Kosovo', 'Montenegro', 'Macedonia', 'Croatia']

gdp_per_capita = [83, 165, 91, 94, 43, 77, 68, 122]

df = pd.DataFrame(list(zip(republics, gdp_per_capita)), columns=['Republic/region', 'GDP per capita (index)'])


# In[181]:


#Explore DF
print(df)


# In[203]:


#Create map with Folium

m = folium.Map(location=[44, 19], tiles= 'cartodbpositron', zoom_start=6)



# In[204]:


#Choropleth

folium.Choropleth(
    geo_data=yugo,
    name='choropleth',
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


# In[191]:


#Create new DF from CSV for points

df_waiss = pd.read_csv('/Users/agustincosovschi/Trabajo/ProduccionPropia/Artículos/WaissEspacial/Visuals/Selection/GDP/Localities_QGIS - Hoja 1.csv')


# In[192]:


lats = []

for lat in df_waiss['Latitude']:
    lats.append(lat)

print(lats)


# In[193]:


longs = []

for lng in df_waiss['Longitude']:
    longs.append(lng)

print(longs)


# In[207]:


locs = []

for loc in df_waiss['Place']:
    locs.append(loc)

print(locs)


# In[208]:


locations = [list(a) for a in zip(lats, longs, locs)]


# In[209]:


print(locations)


# In[210]:


#Introduce points in map M

for location in locations:    
    folium.Marker([location[0],location[1]], popup=location[2],
                  icon=folium.Icon(color='darkred', icon='user')
                 
                 ).add_to(m)
    

    
m


# In[1]:


#Save map

m.save('/Users/agustincosovschi/Trabajo/ProduccionPropia/Artículos/WaissEspacial/Visuals/Selection/GDP/WaissXGDP_User.html')


# In[ ]:





# In[ ]:




