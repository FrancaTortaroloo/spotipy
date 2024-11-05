# %%
import api_connection as api

sp = api.credenciales()
# %%
resultados = sp.artist_albums("https://open.spotify.com/intl-es/artist/6XyY86QOPPrYVGvF9ch6wz?si=OcdpDJMlSECx7RWpjoFP5g", album_type = 'album')
#%%
print(resultados)
#print(resultados.items())
# %%
print(resultados["total"])
# %%
resultados["items"][0]

# %%
for e in resultados["items"][3].items():
    print(e)
# %%
