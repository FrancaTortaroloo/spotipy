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
                'track_id': track['id'],
                'album': album_name,
                'album_release_date': album_release_date,
                'track_name': track['name'],
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
                'track_id': track['id'],
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

# Crear tabla

def tabla_artist_tracks():
    db = mysql.connector.connect(
        host=os.getenv('MYSQL_HOST'),
        port=int(os.getenv('MYSQL_PORT')),
        user=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD'),
        database = os.getenv('MYSQL_DATABASE')
    )
    
    cursor = db.cursor()
    
    try:
        cursor.execute(""" 
    CREATE TABLE artist_tracks (
	track_id VARCHAR(255) PRIMARY KEY,
    album VARCHAR (255),
    album_release_date DATE,
    track_name VARCHAR(255)    
)""")
        print(cursor)
    except my.sql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)

#Tabla track_features

def tabla_track_features():
    db = mysql.connector.connect(
        host=os.getenv('MYSQL_HOST'),
        port=int(os.getenv('MYSQL_PORT')),
        user=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD'),
        database = os.getenv('MYSQL_DATABASE')
    )
    
    cursor = db.cursor()
    
    try:
        cursor.execute(""" 
        CREATE TABLE track_features (
	    track_id VARCHAR(255),
        track_name VARCHAR(255),
        artist VARCHAR(255),
        danceability FLOAT,
        energy FLOAT,
        loudness FLOAT,
        speechiness FLOAT,
        instrumentalness FLOAT,
        valence FLOAT,
        duration_ms INT,
        PRIMARY KEY (track_id),
        FOREIGN KEY (track_id) REFERENCES artist_tracks(track_id)
)
   """)
        print(cursor)
    except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)

## Insertar datos en las tablas 

def insert_into_table(data, table, column_names):
    db = mysql.connector.connect(
        host=os.getenv('MYSQL_HOST'),
        port=int(os.getenv('MYSQL_PORT')),
        user=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD'),
        database = os.getenv('MYSQL_DATABASE')
    )
    
    cursor = db.cursor()
    
    #Seleccionar las columnas de la tabla
    cursor.execute(f"SELECT * from {table} LIMIT 0; ")
    column_names = cursor.column_names
    cursor.fetchall()
    
    insert_query = f"INSERT INTO {table} ({', '.join(column_names)}) VALUES ({', '. join(['%s' for _ in column_names])})"
    values = [tuple(row) for row in data]
    
    # .executemany ejecuta el query INSERT INTO con cada uno de los elementos de "values"
    
    cursor.executemany(insert_query, values)
    
    #guardar los resultados
    
    db.commit()
    
    print(f"Añadidas: {cursor.rowcount} filas")
    
    cursor.fetchall() #vaciar el cursor
    cursor.close()
    db.close()
    
    



             

    