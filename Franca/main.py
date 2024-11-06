#%%
import api_spotify_soporte as api
#%%

sp = api.credenciales()

albumes_lp = sp.artist_albums("https://open.spotify.com/intl-es/artist/6XyY86QOPPrYVGvF9ch6wz?si=UNSuzA5zRGCs5dM8NHj91A", include_groups= 'album')
#%%
print(albumes_lp)
# %%
albumes_lp.keys()
# %%
albumes_lp['items'][0]['album_group']
# %%

nombre_album = []

for nombre in albumes_lp['items']:
    nombre_album.append(nombre['name'])
# %%
print(nombre_album)
# %%
