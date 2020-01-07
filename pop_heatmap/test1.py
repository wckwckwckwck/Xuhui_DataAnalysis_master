import folium
import pandas as pd
import webbrowser
filePath="shanghai.json"
population_data=pd.read_excel("24_population.xlsx")
m_china = folium.Map(location=[35.0896,118.2321], zoom_start=8)




square=folium.Rectangle(
     bounds=([31.18448286,121.4306865],[31.18718238,121.4177114])
).add_to(m_china)

lat_min=31.18223389
lat_max=31.20983599
lon_min=121.4177114
lon_max=121.4842778
delta_lat=lat_max-lat_min
delta_lon=lon_max-lon_min



m_china.save('3.html')
webbrowser.open('3.html')
