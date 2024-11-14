#%%
import api_spotify_soporte as api
import requests
import json
import mysql.connector
from mysql.connector import errorcode
import pandas as pd
#%%
#extraer albumes de linkin park
sp = api.credenciales()

#%%
albumes_lp = sp.artist_albums("https://open.spotify.com/intl-es/artist/6XyY86QOPPrYVGvF9ch6wz?si=UNSuzA5zRGCs5dM8NHj91A", include_groups= 'album')

#%%
#print(json.dumps(albumes_lp, indent = 4))
# %%
dicc_lp = api.extraer_info(albumes_lp)
dicc_lp
#%%
id_canciones = api.obtener_tracks(sp, dicc_lp['id_album'])
id_canciones
#%%
track_data = api.audio_features(sp, id_canciones)
#%%
track_data
#%%
csv = api.convertir_csv(dicc_lp, filename= 'albumes_lp.csv')
csv

csv2 = api.convertir_csv(album_tracks, filename= 'album_tracks.csv')
csv2

# %%
