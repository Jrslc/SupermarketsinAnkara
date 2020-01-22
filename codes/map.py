import folium
import csv
import pandas as pd 
from folium.plugins import MarkerCluster

## ith open da ki csv dosyasını ilçelere göre değiştir. tek tek haritayı çıkar, ilçe dışında kalan marketleri csv dosyalarından at. 

AnkaraMap = folium.Map(location=[39.933365, 32.859741], zoom_start= 9)

with open('Altındag.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= row[0], tooltip= "Altindag").add_to(AnkaraMap)

with open('SupermarketsinAyas.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= row[0], tooltip= "Ayas").add_to(AnkaraMap)
with open('Bala.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= row[0], tooltip= "Bala").add_to(AnkaraMap)

with open('Beypazari.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= row[0], tooltip= "Beypazari").add_to(AnkaraMap)       

with open('Cankaya.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= row[0], tooltip= row[0]).add_to(AnkaraMap)  

with open('Camlidere.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= row[0], tooltip= row[0]).add_to(AnkaraMap)

with open('Çubuk.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= row[0], tooltip= row[0]).add_to(AnkaraMap) 
with open('Elmadag.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= row[0], tooltip= row[0]).add_to(AnkaraMap) 
with open('Etimesgut.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= row[0], tooltip= row[0]).add_to(AnkaraMap)
with open('Evren.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= row[0], tooltip= row[0]).add_to(AnkaraMap)
with open('Güdül.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= row[0], tooltip= row[0]).add_to(AnkaraMap) 
with open('haymana.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= row[0], tooltip= row[0]).add_to(AnkaraMap) 
with open('Kalecik.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= row[0], tooltip= row[0]).add_to(AnkaraMap) 
with open('Kahramankazan.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= row[0], tooltip= row[0]).add_to(AnkaraMap) 
with open('Kecıoren.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= row[0], tooltip= row[0]).add_to(AnkaraMap)
with open('Kızılcahamam.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= row[0], tooltip= row[0]).add_to(AnkaraMap)

with open('Mamak.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= row[0], tooltip= row[0]).add_to(AnkaraMap) 
with open('Nallıhan.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= row[0], tooltip= row[0]).add_to(AnkaraMap)
with open('polatlı.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= row[0], tooltip= row[0]).add_to(AnkaraMap)
with open('Pursaklar.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= row[0], tooltip= row[0]).add_to(AnkaraMap)
with open('Sereflıkochısar.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= row[0], tooltip= row[0]).add_to(AnkaraMap)
with open('sincan.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= row[0], tooltip= row[0]).add_to(AnkaraMap)
with open('Yenimahalle.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= row[0], tooltip= row[0]).add_to(AnkaraMap)

with open('Golbasi.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= row[0], tooltip= row[0]).add_to(AnkaraMap)


##trying geo map for Ankara

stateLevel_data = "Ankarailce.csv"
state_data = pd.read_csv(stateLevel_data)
state_geo = "turkiye-ilceler.geojson" ##statelevel data 


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
).add_to(AnkaraMap)




AnkaraMap.save("AnkaraMap.html")