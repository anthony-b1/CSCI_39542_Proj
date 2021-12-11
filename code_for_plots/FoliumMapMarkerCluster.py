#Reference: https://medium.com/analytics-vidhya/generating-maps-with-python-maps-with-markers-part-2-2e291d987821
import pandas as pd
import folium
from folium import plugins 

df = pd.read_csv('Specific_Cols.csv') 
df['CMPLNT_FR_DT'] = pd.to_datetime(df['CMPLNT_FR_DT'])
#Filtering only 2019
#mask = (df['CMPLNT_FR_DT'] < '2020-1-1') 
#Filtering only 2020
#mask = (df['CMPLNT_FR_DT'] >= '2020-1-1') & (df['CMPLNT_FR_DT'] < '2021-1-1')
#Filtering only 2021
mask = (df['CMPLNT_FR_DT'] >= '2021-1-1') & (df['CMPLNT_FR_DT'] < '2022-1-1')
df = df.loc[mask]
print(df)

nyc_map = folium.Map(location=[40.7128, -74.006], zoom_start=11)

incidents = plugins.MarkerCluster().add_to(nyc_map)

for lat, lng, label, in zip(df.Latitude, df.Longitude, df.OFNS_DESC):
    folium.Marker(
    location=[lat, lng],
    icon=None,
    popup=label,
).add_to(incidents)

nyc_map.save('Folium2021MarkerCluster.html')