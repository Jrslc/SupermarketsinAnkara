## getting csv files into one file
import csv
import folium
import pandas as pd 



##trying geo map for Ankara

stateLevel_data = "Ankarailce.csv"
state_data = pd.read_csv(stateLevel_data)
state_geo = "turkiye-ilceler.geojson" ##statelevel data 

townlevelmap = folium.Map(location=[39.933365, 32.859741], zoom_start= 3)


folium.Choropleth(
    geo_data=state_geo,
    name='choropleth',
    data=state_data,
    columns=['name', 'Supermarkets'],
    key_on='properties.name',
    fill_color='BuPu',
    fill_opacity=0.7,
    line_opacity=1,
    legend_name='NumberOfSupermarkets' 
).add_to(townlevelmap)

townlevelmap.save("townlevelmap.html")


