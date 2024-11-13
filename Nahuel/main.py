# %%
import api_func as api
sp = api.credenciales()
import pandas as pd
#%% 
prueba = api.obtener_tracks(sp=sp, id_albums='494aUGKXMH5ruXtR3O1a3H')
# %%
id_albums = [['494aUGKXMH5ruXtR3O1a3H']]


album_tracks = api.obtener_tracks(sp, id_albums)
# %%
album_tracks
# %%
album_id = '494aUGKXMH5ruXtR3O1a3H'
canciones = api.song_album(sp, album_id)
print(canciones)
# %%
canciones
#%%
asd = api.song_info(sp, canciones)


# %%
asd
# %%
df = pd.DataFrame(asd)
# %%
df
# %%
