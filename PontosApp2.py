import folium as fm
from folium.plugins import LocateControl
from folium.plugins import MeasureControl
from folium.plugins import MousePosition
from folium.plugins import MiniMap


#from folium.plugins import Search



## Mapa principal
mapa = fm.Map(location=[-15.79371, -47.88141],
              zoom_start=11.5,
              min_zoom=10)
## Camadas de mapas
esri = fm.TileLayer(name='Imagem de Satélite Esri',min_zoom=10,
                    tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                    location=[-15.79371, -47.88141],
                    attr='Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, '
                         'Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community').add_to(mapa)
cartoDB = fm.TileLayer(name='Vetorial CartoDB Voyager',
                       tiles='https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png',
                       location=[-15.79371, -47.88141],
                       min_zoom=10,
                       attr='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> '
                            'contributors &copy; <a href="https://carto.com/attributions">CARTO</a>').add_to(mapa)
## Controle de camadas
fm.LayerControl().add_to(mapa)

## Plugins
posicaolocal = LocateControl().add_to(mapa)
medidordistancia = MeasureControl(position='topleft').add_to(mapa)
posicaomouse = MousePosition().add_to(mapa)
mapapeq = MiniMap().add_to(mapa)

# pesquisa = Search().add_to(mapa) (ESSE PUGLINS FUNCIONARÁ INTEGRADO COM A CAMADA MARCADORES)

## Impressão do Mapa
mapa.save('PontosAppWeb.html')
