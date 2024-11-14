import csv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv

load_dotenv()


def credenciales():
    
    CLIENT_ID = os.getenv("client_id")
    CLIENT_SECRET = os.getenv("client_secret")
    
    credenciales = SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET)
    sp = spotipy.Spotify(client_credentials_manager = credenciales)
    
    return sp


def extraer_info(diccionario):

    linkin_park = {'id_album': [],
    'nombre_album': [],
    'cant_tracks': [],
    'release_date': []}
    
    for id in diccionario['items']:
        linkin_park['id_album'].append([id['id']])
        linkin_park['nombre_album'].append(id['name'])
        linkin_park['cant_tracks'].append(id['total_tracks'])
        linkin_park['release_date'].append(id['release_date'])
        
    return linkin_park


def obtener_tracks(sp, id_albums):
    
    #creo un diccionario para almacenar los IDs de los albumes y los tracks
    album_tracks = {}
    
    #extraer los nombres de los tracks de cada album
    for a_id in id_albums:
        a_id = a_id[0] #extraer el id del album desde la lista 
        tracks = sp.album_tracks(a_id)
        
        #creo una lista para almacenar los nombres de las pistas
        tracks_info = []
   
        for t in tracks['items']:
            tracks_info.append({
                'track_name': t['name'],
                'track_id': t['id']
            })
        
        #asociar el ID del álbum con tracks_names
        album_tracks[a_id] = tracks_info
    
    return album_tracks
    


def audio_features(sp, album_tracks):
    
    #crear una lista para almacenar los datos en un formato compatible con DF
    track_data = []

    #iterar sobre album y track
    for album_id, tracks in album_tracks.items():
        for track in tracks:
            track_id = track['track_id']

            #obtener los audios features
            #la funcion devuelve una lista, se toma el primer elemento
            features = sp.audio_features([track_id])[0]
            
            if features is not None:
            #extraer la info 
                track_info = {
                    'album_id': album_id,
                    'track_name': track['track_name'],
                    'track_id': track['track_id'],
                    'danceability': features.get('danceability'),
                    'duration_ms': features.get('duration_ms'),
                    'energy': features.get('energy'),
                    'instrumentalness': features.get('instrumentalness'),
                    'loudness': features.get('loudness'),
                    'speechiness': features.get('speechiness'),
                    'tempo': features.get('tempo'),
                    'valence': features.get('valence')

                }
            else:
                # Completa con None si no hay features disponibles
                track_info = {
                    'album_id': album_id,
                    'track_name': track['track_name'],
                    'track_id': track['track_id'],
                    'danceability': None,
                    'duration_ms': None,
                    'energy': None,
                    'instrumentalness': None,
                    'loudness': None,
                    'speechiness': None,
                    'tempo': None,
                    'valence': None
                }
                
                #agregar e diccionario de la canción a la lista
                track_data.append(track_info)
                
    return track_data


def convertir_dicc(dicc, filename):
    #obtener las claves para usarlas como encabezados
    keys = dicc.keys()
    
    #abrir archivo csv para escribir
    with open (filename, mode = 'w', newline = '')as file:
        writer = csv.writer(file)
        
        #nombre de las columnas
        writer.writerow(keys)
        
        #completar las filas con los datos
        rows = zip(*dicc.values())
        writer.writerows(rows)
        
    print(f'{filename}')


#def convertir_csv(album_tracks, filename):

    



             

    