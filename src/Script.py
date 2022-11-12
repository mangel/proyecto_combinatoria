#### Parte 1. Graficar los puntos

## Paquetes necesarios

import pandas as pd
import plotly.express as px
import plotly.io as pio
pio.renderers.default='browser'
import plotly.graph_objects as go


## Data import

df = pd.read_csv('GeoLoc.txt',sep="\t")
#crs = {'init': 'epsg:4326'}
#geometry = [Point(xy) for xy in zip(df['Longitud'],df['Latitud'])]
fig = px.scatter_geo(df,lat='Latitud',lon='Longitud', hover_name="Lugar")
#fig.update_layout(title = 'World map', title_x=0.5, geo_scope = 'south america')
fig.update_geos(
    visible=False, resolution=50, scope="south america",
    showcountries=True, countrycolor="Black",
    showsubunits=True, subunitcolor="Blue"
)
fig.show()

## Cálculo de distancias


