#Name: Dante Rivera
#Date: September 28th
#Creates a map of nyc of collisions


import folium  #Using folium to make the maps
import pandas as pd  #panda to read csv
import math # Check if values are nan, because panda doesn't like that
import time # Timing execution as it's a large file, will limit it to 10k entries though

c_f = input('Enter CSV file name:    ')
o_f = input('Enter an output file name:  ')

start = time.time()
df = pd.read_csv(c_f)

#Creating a map
mapCUNY = folium.Map(location=[40.75, -74.125], zoom_start=10)

lat = df["LATITUDE"]
lon = df["LONGITUDE"]
print(lat)
print(lon)
# newMarker = folium.Marker([lat, lon]).add_to(mapCUNY)


for i in range(22116):
    newMarker = folium.Marker([lat, lon]).add_to(mapCUNY)

#Saving the created map:
mapCUNY.save(outfile=o_f)


end = time.time()
print(end - start)
