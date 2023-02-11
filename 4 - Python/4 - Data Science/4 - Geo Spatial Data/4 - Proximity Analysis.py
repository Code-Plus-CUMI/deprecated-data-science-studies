import folium
from folium import Marker, GeoJson
from folium.plugins import HeatMap

# to create MultiPolygons
from shapely.geometry import MultiPolygon

import pandas as pd
import geopandas as gpd

def embed_map(m, file_name):
	"""
	Allows to display maps in any browser
	"""
    from IPython.display import IFrame
    m.save(file_name)
    return IFrame(file_name, width='100%', height='500px')

"""
	Proximity Analysis

	1 - Calculating Distance Between Points

It's used to literally calculate the distance between
two points.

/ First, if we'll be working with two different
GeoDataFrames, both of them gotta be in the same
CRS Code. You can check it out with the following code:

	print(stations.crs)
	print(accidents.crs)

/ If necessary you can change the CRS with the code:

	stations.crs = {'init' : 'epsg:4326'}
	accidents.crs = {'init' : 'epsg:4326'}
"""

distance = stations.iloc[31].geometry.distance(accidents.iloc[29].geometry)
distances = stations.geometry.distance(accidents.iloc[29].geometry)

#######

"""
	2 - Buffer

It's used to check out if a point is in a especific 
radius
"""

# the stations.crs is using feet as the unit.
# so, to convert feet to unit, we gotta
# multiply 5280 by 2
two_mile_buffer = stations.geometry.buffer(2*5280)
ten_km_buffer = stations.geometry.buffer(10*1000)

# creating the map to show the radious and the points
map_1 = folium.Map(
	location=[39.9526, -75.1652]
	, tile='openstreetmap'
	, zoom_start=11
)

HeatMap(
	data=[accidents['Latitude'], accidents['Longitude']]
	, radius=15
).add_to(map_1)

for index, row in stations.iterrows():
	Marker([row['Latitude'], row['Longitude']]).add_to(map_1)

GeoJson(two_mile_buffer.to_crs(epsg=4326)).add_to(map_1)

# pop up with the latitude and longitude
# when you tap any location in the map
folium.LatLngPopup().add_to(map_1)

map_1

# now, to be able to check out if an accident occured
# in a radius of 2 miles from each station in a easier
# way (without having the need to check out the map plot)
# we can create a MultiPolygon of the radius

multi_polygon = two_mile_buffer.geometry.unary_union
multi_polygon

multi_polygon.contains(accidents.iloc[29].geometry)
# > True (the accident occured in the radius)

multi_polygon.contains(accidents.iloc[31].geometry)
# > False (the accident DIDN'T occured in the radius)