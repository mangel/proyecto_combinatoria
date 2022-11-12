#### Parte 1. Graficar los puntos

## Paquetes necesarios

import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Point, Polygon
import descartes

## Mapa Medellín

Med = gpd.read_file('BarrioVereda_2014.shp')
fig,ax = plt.subplots(figsize = (15,15))
Med.plot(ax = ax)

## Data import

df = pd.read_csv('GeoLoc.txt',sep="\t")
crs = {'init': 'epsg:4326'}
geometry = [Point(xy) for xy in zip(df['Longitud'],df['Latitud'])]

## Generate gpd_df

geo_df = gpd.GeoDataFrame(df,crs = crs, geometry = geometry)

geo_df.plot(ax = ax, markersize = 20, color = "red", marker = "o")

for i in range(20):
    plt.annotate(s=df.iloc[i,0],xy=[df.iloc[i,2],df.iloc[i,1]])