#%%
import api_spotify_soporte as api
import requests
import json
import mysql.connector
from mysql.connector import errorcode

#%%
#extraer albumes de linkin park
sp = api.credenciales()

#%%
albumes_lp = sp.artist_albums("https://open.spotify.com/intl-es/artist/6XyY86QOPPrYVGvF9ch6wz?si=UNSuzA5zRGCs5dM8NHj91A", include_groups= 'album')

#%%
print(json.dumps(albumes_lp, indent = 4))
# %%
dicc_lp = api.extraer_info(albumes_lp)
dicc_lp
#%%

album_tracks = api.obtener_tracks(sp, id_albums = dicc_lp['id_album'])
album_tracks

#%%
info_canciones = api.song_info(sp, )
#%%
csv = api.convertir_csv(album_tracks)
csv
#%%

csv1 = api.dicc_csv(dicc_lp)
csv1

#%%



