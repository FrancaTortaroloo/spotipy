import csv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
import requests
from dotenv import load_dotenv
import json
import mysql.connector
from mysql.connector import errorcode
import pandas as pd
import re
from datetime import datetime


load_dotenv()


def credenciales():
    
    CLIENT_ID = os.getenv("client_id")
    CLIENT_SECRET = os.getenv("client_secret")
    
    credenciales = SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET)
    sp = spotipy.Spotify(client_credentials_manager = credenciales)
    
    return sp


def url_artista(url):
    match = re.search(r'artist/([a-zA-Z0-9]+)', url)
    if match:
        return match.group(1)
    else:
        print("URL no válida.")
        return None


def get_artist_tracks(sp, artist_url, csv_filename = 'artist_tracks.csv'):
    #obtiene toda la info de albumes y canciones del artista con su URL y lo guarda en un csv
    #ID del artista a partir de la URL
    artist_id = url_artista(artist_url)
    if not artist_id:
        print('ID del artista no encontrado')
        return
    
    all_tracks = []
    #obtener albumes del artista
    albums = sp.artist_albums(artist_id, album_type = ['album', 'single'])
    album_items = albums['items']
    
    
    
    for album in album_items:
        album_id = album['id']
        album_name = album['name']
        album_release_date = album['release_date']
        album_tracks = sp.album_tracks(album_id)['items']
        
        for track in album_tracks:
            track_info = {
                'album': album_name,
                'album_release_date': album_release_date,
                'track_name': track['name'],
                'track_id': track['id']
            }
            all_tracks.append(track_info)
            
    #guardar los datos en csv 
    
    df_tracks = pd.DataFrame(all_tracks)
    df_tracks.to_csv(csv_filename, index = False)
    print(f'Datos de albumes y canciones guardados en {csv_filename}')
    
    return df_tracks #devolver el df por si se necesita hacer mas operaciones

def get_track_features(sp, track_ids, csv_filename = 'track_features.csv'):
    #obtiene los features de una lista de canciones y lo guarda en un csv
    
    all_features = []
    
    for track_id in track_ids:
        track = sp.track(track_id)
        features = sp.audio_features(track_id)[0]
        
        if features: #evitar errores si no hay caracteristicas disponibles
            track_features = {
                'id_track': track['id'],
                'track_name': track['name'],
                'artist': [artist['name'] for artist in track['artists']],
                'danceability': features['danceability'],
                'energy': features['energy'],
                'loudness': features['loudness'],
                'speechiness': features['speechiness'],
                'intrumentalness': features['instrumentalness'],
                'valence': features['valence'],
                'duration_ms': features['duration_ms']
            }
            
            all_features.append(track_features)
            
    #Guardar los datos en un csv
    df_features = pd.DataFrame(all_features)
    df_features.to_csv(csv_filename, index = False)
    print(f'Datos de features guardados en {csv_filename}')
    
    return df_features

#lo comento porque la bbdd ya esta creada
'''

def creacion_bbdd():
    cnx = mysql.connector.connect(user= os.getenv('MYSQL_USER'), password= os.getenv('MYSQL_PASSWORD'),
                              host=os.getenv('MYSQL_HOST'))
    mycursor = cnx.cursor()
    
    try:
        mycursor.execute("CREATE DATABASE BD_linkin_park")
        print(mycursor)
    except mysql.connector.Error as err:
        print(err)
        print("Error Code:", err.errno)
        print("SQLSTATE", err.sqlstate)
        print("Message", err.msg)
'''

def creacion_tablas():
    cnx = mysql.connector.connect(database='BD_pruebas')
    mycursor = cnx.cursor()
    try:
        mycursor.execute("CREATE TABLE artist_tracks (album VARCHAR(255), album_release_date DATE, track_name VARCHAR(255), track_id VARCHAR(255))")
        print(mycursor)
    except mysql.connector.Error as err:
        print(err)
        print("Error Code:", err.errno)
        print("SQLSTATE", err.sqlstate)
        print("Message", err.msg)
    
    



             

    