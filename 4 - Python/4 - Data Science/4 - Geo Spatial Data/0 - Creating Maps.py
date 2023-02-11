"""
	Creating Maps

	GeoPandas (GPD) is the library to read dataframes
that contain Geo Spatial Datas (Geommetry) in the columns.
In general, the Spatial Datas can be one of the three below:

	/ Point: used to represent a location/spot in the map
	Attributes: point_gdf.x | point_gdf.y

	/ Line: used to represent streets
	Attributes: line_gdf.length

	/ Polygon: used to represent boundaries
	Attributes: polygon_gdf.area
"""

# Reading two Geo Spatial Datasets
# the first one is a general map while the second
# one is locations into the first
import geopandas as gpd

filepath_1 = gpd.datasets.get_path('dataset_1_name.shp')
world = gpd.read_file(filepath_1)
world = geo_df.loc[:, ['CLASS', 'COUNTRY', 'GEOMETRY']].copy()

filepath_2 = gpd.datasets.get_path('dataset_2_name.shp')
world_loans = gpd.read_file(filepath_2)

# Plotting a map with the two datasets: all of the loans
# around the world
#
# color >> background color of the territories
# edgecolor >> the name explains itself
# zorder >> it's like the 'z' attribute in css
ax = world.plot(figsize=(10, 10)
				, color='none'
                , edgecolor='black'
                , zorder=0)

world_loans.plot(color='red', markersize=3
				, ax=ax, zorder=1)

###########

# Plotting all of the loans in Philippines
PHL_world = world.loc[world.COUNTRY == 'Philippines'].copy()
PHL_loans = world_loans.loc[world_loans.COUNTRY == 'Philippines'].copy()

ax = PHL_world.plot(figsize=(10,10)
					, color='none'
					, edgecolor='black'
					, zorder=0)

PHL_loans.plot(color='red', markersize=5, ax=ax)