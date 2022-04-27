# encoding: utf-8

##################################################
# This script shows uses the pandas library to visualise geospatial data sets
##################################################
#
##################################################
# Author: Diego Pajarito
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Maintainer: Diego Pajarito
# Email: diego.pajarito@iaac.net
# Status: development
##################################################

# We need to import pandas library as well as the plot libraries matplotlib and seaborn
import pandas as pd
import geopandas
import matplotlib.pyplot as plt
from shapely.geometry import Point

# We read the file from Open Data Barcelona
# https://opendata-ajuntament.barcelona.cat/data/en/dataset/metadades-estacions-meteorologiques/resource/feafec8a-b389-42b5-a85d-cf16f3976440
url = 'https://opendata-ajuntament.barcelona.cat/data/dataset/82dc847a-661d-4701-a582-b0c1aba89b2a/resource/feafec8a-b389-42b5-a85d-cf16f3976440/download'
bcn_stations = pd.read_csv(url)


# Setting up the geospatial features
crs = {'init': 'epsg:4326'}
geometry = [Point(xy) for xy in zip(bcn_stations["LONGITUD"], bcn_stations["LATITUD"])]
bcn_stations_geo = geopandas.GeoDataFrame(bcn_stations, crs=crs, geometry=geometry)

# To plot multiple layers we need to use subplots
f, ax = plt.subplots()
bcn_stations_geo.plot(ax=ax, marker='o', color='blue', markersize=20)
plt.show()

