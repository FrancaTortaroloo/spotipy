import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv

load_dotenv()

def credenciales ():
    CLIENT_ID = os.getenv("client_id")
    CLIENT_SECRET = os.getenv("client_secret")
    
    credenciales = SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET)
    sp = spotipy.Spotify(client_credentials_manager = credenciales)
    
    return sp

def preparamos_url(link):
    return link.split("/"[-1].split("?")[0])

def obtener_tracks(sp, id_albums):
    
    #creo un diccionario para almacenar los IDs de los albumes y los tracks
    album_tracks = {}
    
    #extraer los nombres de los tracks de cada album
    for a_id in id_albums:
        a_id = a_id[0] #extraer el id del album desde la lista 
        tracks = sp.album_tracks(a_id)
        
        #creo una lista para lamacenar los nombres de las pistas en una lista
        tracks_names = []
        tracks_id = []
        for t in tracks['items']:
            tracks_names.append(t['name'])
            tracks_id.append(t['id'])        
        #asociar el ID del álbum con tracks_names
        album_tracks[a_id] = tracks_names, tracks_id
    
    return album_tracks

def song_album(album_id):
    
    # Obtiene las canciones del álbum
    results = sp.album_tracks(album_id)
    tracks = results['items']

    # Construye un diccionario con el nombre de la canción como clave y el ID como valor
    track_dict = {track['name']: track['id'] for track in tracks}

    return track_dict

def song_info(track_dict):
    
    # Lista para almacenar los IDs de las canciones
    track_ids = list(track_dict.values())
    
    # Llama al endpoint para obtener características de audio de varias canciones
    audio_features_list = sp.audio_features(tracks=track_ids)

    # Construye un diccionario con el nombre de la canción y sus características de audio
    audio_features_dict = {
        track_name: features
        for track_name, features in zip(track_dict.keys(), audio_features_list)
    }

    return audio_features_dict

