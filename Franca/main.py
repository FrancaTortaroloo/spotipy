#%%
import api_spotify_soporte as api
import test_connection as connection
#%%
#extraer albumes de linkin park
sp = api.credenciales()

#%%
artist_url = 'https://open.spotify.com/intl-es/artist/6XyY86QOPPrYVGvF9ch6wz?si=UNSuzA5zRGCs5dM8NHj91A'

#%%
tracks_artist = api.get_artist_tracks(sp, artist_url)
tracks_artist
#%%
#obtener id de canciones 
track_ids = tracks_artist['track_id'].tolist()
features_df = api.get_track_features (sp, track_ids)
#%%
sql = connection.test_connection()
# %%
crear_bbdd = api.conexion_sql()

#%%
len(df_tracks)

# %%
