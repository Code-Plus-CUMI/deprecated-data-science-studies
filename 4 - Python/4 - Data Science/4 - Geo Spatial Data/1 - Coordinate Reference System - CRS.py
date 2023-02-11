"""
	Coordinate Reference System (CRS)

	CRS's are the various ways we can project a map,
especially the Earth!! Each projection (represented as
codes in CRS) is useful for a especific task (but don't
be a fool too learn and memorize every single one, just
learn them when needed, ok?)
	
	When reading 'shp' files with geopandas, it sets the
CRS as 32630 (the projection that everyone is used to
see in the books), however, when reading 'csv' files,
pandas can't set the CRC, which means, we gotta first
read the file with pandas, after that transform into
GeoDataFrame with geopandas and finally set the CRC.
"""

import pandas as pd
import geopandas as gpd

df_points = pd.read_csv('filepath.csv')

geo_df_points = gpd.GeoDataFrame(df_points
							   , geometry=gpd.points_from_xy(
									df_points.Longitude, df_points.Latitude
						  		 )
)

#geo_df_points.crs = {'init' : 'epsg:32630'}
geo_df_points.crs = {'init' : 'epsg:4326'}

"""
Also, when you wish to plot to GeoDataFrames together,
like the world boundaries and some points or lines in it,
you gotta make sure that both DataFrames are in the same
CRS code.

Else, you'll need to convert one or both of them to the
same CRS using the 'to_crs' function.
"""

geo_df_world = gpd.read_file('filepath.shp')

ax = geo_df_world.plot(
		figsize=(10,7)
		, color='none'
		, edgecolor='black'
		, linestyle=':'
		, zorder=0
)

geo_df_points.to_crs(epsg=32630)
			 .plot(
			 	color='red'
			 	, markersize=5
			 	, ax=ax
			 )