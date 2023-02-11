import pandas as pd
import geopandas as gpd
import numpy as np

import folium
from folium import Marker

"""
	Manipulating Geo Spatial Data

	1 - Geo Encoding

	Geo Encoding is the process to transform a place's 
name into a localization in the map.

	In a nutshell, it's like you search one place
on GPS or even on Google Maps by name, and the software
gives you the localization of this place.
"""

# library to make the Geo Encoding
from geopy.geocoders import Nominatim

# Creating the Geolocator and Getting the POint and Address #
geolocator = Nominatim(user_agent='kaggle_user')
location = geolocator.geocode('Pyramid of Khufu')


print(location.address) # street, number, district...
print(location.point) # latitude and longitude
print(location.point.latitude) # latitude
print(location.point.longitude) # longitude

# Example - Reading Universities dataframe and plotting their
# localization into a map

universities = pd.read_csv('filepath.csv')

def my_geocoder(row):
	"""
	Given a place's name, this function
	returns the latitude and longitude of
	the place.

	If can't find the place, returns None/NaN.
	"""

	try:
		point = geolocator.geocode(row).point
		return pd.Series(
					{
						'Latitude'    : point.latitude
						, 'Longitude' : point.longitude
					}
				)

	except: return None

universities[['Latitude', 'Longitude']] = universities.apply(lambda x: my_geocoder(x['Name']), axis=1)
universities = universisties.loc[~np.isnan(universities['Latitude'])]
# universities = universisties.loc[universities['Latitude'] is not None)]

universities = gpd.GeoDataFrame(
	universities
	, geometry=gpd.points_from_xy(universities.Longitude, universities.Latitude)
)

universities.crs = {'init' : 'epsg:4326'}

universities_map = folium.Map(
	location=[54,15]
	, tiles='openstreetmap'
	, zoom_start=5
)

for index, row in universities.iterrows():
	Marker(
		[row['Latitude'], row['Longitude']]
	).add_to(universities_map)

universities_map

###########

"""
	2 - Joining Geo Data Frames

We can make the joining in two different ways:

	/ Attribute Join: we merge two dataframes
using a common column between them

		gdf_3 = gdf_1.merge(gdf_2, on='common_column')

	/ Spatial Join: we merge two dataframes
using the geometry (latitude and longitude) column:

		gdf_3 = gpd.sjoin(gdf_1, gdf_2)
"""

# upgrade rows without having to drop and add the values again
df.update()