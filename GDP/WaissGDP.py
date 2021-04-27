#!/usr/bin/env python
# coding: utf-8

# In[177]:


import folium
from folium.features import CustomIcon
import json
import pandas as pd
import geopandas as gpd


# In[178]:


#Leer el geojson file con geopandas

yugo = gpd.read_file('/Users/agustincosovschi/Trabajo/ProduccionPropia/Artículos/WaissEspacial/Visuals/Selection/GDP/yugo.geojson')


# In[179]:


#Explorar el geojson 

print(yugo.head(25))


# In[180]:


#Meto mis datos de un csv

republics = ['Bosnia and Herzegovina', 'Slovenia', 'Serbia', 'Vojvodina', 'Kosovo', 'Montenegro', 'Macedonia', 'Croatia']

gdp_per_capita = [83, 165, 91, 94, 43, 77, 68, 122]

df = pd.DataFrame(list(zip(republics, gdp_per_capita)), columns=['Republic/region', 'GDP per capita (index)'])


# In[181]:


#Exploro el csv
print(df)


# In[203]:


#Hago el mapa

m = folium.Map(location=[44, 19], tiles= 'cartodbpositron', zoom_start=6)



#colores : ‘scheme_info = {'BuGn': 'Sequential',
           #        'BuPu': 'Sequential',
            #       'GnBu': 'Sequential',
             #      'OrRd': 'Sequential',
              #     'PuBu': 'Sequential',
               #    'PuBuGn': 'Sequential',
                #  'PuRd': 'Sequential',
                 #  'RdPu': 'Sequential',
                 #  'YlGn': 'Sequential',
                  # 'YlGnBu': 'Sequential',
                   #'YlOrBr': 'Sequential',
            #       'YlOrRd': 'Sequential',
             #      'BrBg': 'Diverging',
              #     'PiYG': 'Diverging',
               #    'PRGn': 'Diverging',
               #    'PuOr': 'Diverging',
                #   'RdBu': 'Diverging',
                #   'RdGy': 'Diverging',
                #   'RdYlBu': 'Diverging',
                #   'RdYlGn': 'Diverging',
                ##   'Spectral': 'Diverging',
                #   'Accent': 'Qualitative',
                #   'Dark2': 'Qualitative',
                #   'Paired': 'Qualitative',
                #   'Pastel1': 'Qualitative',
                #   'Pastel2': 'Qualitative',
                #   'Set1': 'Qualitative',
                #   'Set2': 'Qualitative',
                #   'Set3': 'Qualitative',
                #   }.'



# In[204]:


#Hago el Choropleth: geo_data es mi geojason, data es mi dataframe, columns son las columnas a rendear, 
#key_on es el key del geojason a tomar

bins = list(df['GDP per capita (index)'].quantile([0, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 1]))
print (bins)


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


for location in locations:    
    folium.Marker([location[0],location[1]], popup=location[2],
                  icon=folium.Icon(color='darkred', icon='user')
                 
                 ).add_to(m)
    

    
m


# In[211]:


m.save('/Users/agustincosovschi/Trabajo/ProduccionPropia/Artículos/WaissEspacial/Visuals/Selection/GDP/WaissXGDP_User.html')


# In[ ]:




