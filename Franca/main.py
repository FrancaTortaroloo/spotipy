#%%
import api_spotify_soporte as api
import test_connection as connection
import pandas as pd
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
#conexion al servidor
sql = connection.test_connection()
# %%
#crear bbdd

crear_bbdd = api.conexion_sql()
#%%
#crear tabla1
tabla = api.tabla_artist_tracks()
#%%
#crear tabla2
track_features = api.tabla_track_features()
#%%
#inserción de datos tabla1

data = pd.read_csv('artist_tracks.csv').values
table = "artist_tracks"
column_names = ["track_id", "album", "album_release_date", "track_name"]

tabla_lp = api.insert_into_table(data = data, table = table, column_names= column_names)
#%%
#inserción de datos tabla2

data = pd.read_csv('track_features.csv').values.tolist() #convertir a lista de listas
table = "track_features"
column_names = ["track_id", "track_name", "artist", "danceability", "energy", "loudness", "speechiness", "instrumentalness", "valence", "duration_ms"]

tabla_2 = api.insert_into_table(data = data, table = table, column_names= column_names)
# %%
