#GeoJSON: https://data.cityofnewyork.us/City-Government/Borough-Boundaries/tqmj-j8zm
import pandas as pd
import json
import plotly.express as px 

df = pd.read_csv('Specific_Cols.csv') 
#Making two columns, one is the borough name and the second is the count of crimes in each borough
newDF = pd.DataFrame()
newDF = df
newDF['CMPLNT_FR_DT'] = pd.to_datetime(newDF['CMPLNT_FR_DT'])

############ Three different filters for the years 2019,2020, and 2021  #####################

#Filtering only 2019
mask = (newDF['CMPLNT_FR_DT'] < '2020-1-1') 
#Filtering only 2020
#mask = (newDF['CMPLNT_FR_DT'] >= '2020-1-1') & (newDF['CMPLNT_FR_DT'] < '2021-1-1')
#Filtering only 2021
#mask = (newDF['CMPLNT_FR_DT'] >= '2021-1-1') 

newDF = newDF.loc[mask]
newDF = newDF['BORO_NM'].value_counts().reset_index()
newDF = newDF.rename({'index':'BORO_NM','BORO_NM':'Count'}, axis=1)
newDF['BORO_NM'] = newDF['BORO_NM'].str.title()

#Load geojson to get the geographical features of the boroughs 
nyBoro = json.load(open('Borough Boundaries.geojson', 'r'))

#See the id of each borough in geojson 
boro_id_map = {}
for feature in nyBoro['features']:
    feature['id'] = feature['properties']['boro_code']
    boro_id_map[feature['properties']['boro_name']] = feature['id']

#Getting the id number of each borough
newDF['id'] = newDF['BORO_NM'].apply(lambda x: boro_id_map[x])

#Making the choropleth map
fig = px.choropleth_mapbox(newDF, locations='id', geojson=nyBoro, color='Count', hover_name='BORO_NM', 
        hover_data=['Count'], mapbox_style='carto-positron', center={'lat': 40.7, 'lon': -74}, opacity=0.5)
fig.show()
fig.write_html('choropleth2019.html')