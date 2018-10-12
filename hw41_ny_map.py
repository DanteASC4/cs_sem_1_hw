#Name: Dante Rivera
#Date: September 28th
#Map of nyc, with marker on hunter

#Using folium to make maps
import folium

#Creating a map
mapCUNY = folium.Map(location=[40.75, -74.125], zoom_start=10)

#Creating a marker for hunter college:
folium.Marker(location = [40.768731, -73.964915], popup = "Hunter College").add_to(mapCUNY)

#Saving the created map:
mapCUNY.save(outfile='nycMap.html')
