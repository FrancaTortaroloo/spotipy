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
        
        #creo una lista para lamacenar los nombres de las pistas en una lista
        tracks_names = []
        for t in tracks['items']:
            tracks_names.append(t['name'])
        
        #asociar el ID del álbum con tracks_names
        album_tracks[a_id] = tracks_names
    
    return album_tracks

def song_info(sp, track_dict):
    # Lista para almacenar los IDs de las canciones
    track_ids = list(track_dict.values())
    
    # Llama al endpoint para obtener características de audio de varias canciones
    audio_features_list = sp.audio_features(tracks=track_ids)

    # Claves que queremos eliminar
    keys_to_discard = ['uri', 'track_href', 'analysis_url']

    # Construye un diccionario con el nombre de la canción y sus características de audio, excluyendo las claves no deseadas
    audio_features_dict = {
        track_name: {k: v for k, v in features.items() if k not in keys_to_discard}
        for track_name, features in zip(track_dict.keys(), audio_features_list)
    }

    return audio_features_dict

def convertir_csv(album_tracks, filename = 'album_tracks.csv'):
    with open(filename, mode= 'w', newline='') as file:
        writer = csv.writer(file)
        
        #columnas
        writer.writerow(['ID Album', 'Track Name'])
        
        #insertar los datos
        for album_id, tracks in album_tracks.items():
            for track in tracks:
                writer.writerow([album_id, track])
                
    print(f'{filename}')


def dicc_csv(dicc, filename = 'albumes_lp.csv'):
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
             

    