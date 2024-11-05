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

#url_playlist = "https://open.spotify.com/intl-es/album/6PFPjumGRpZnBzqnDci6qJ?si=iqQRrwOpSz2I7JeKbwuS2g"
#print(url_playlist.split("/")[-1].split("?")[0])

def preparamos_url(link):
    return link.split("/"[-1].split("?")[0])

def album_info(album):
    # Imprimir detalles del álbum
    print("Detalles del Álbum")
    print("------------------")
    print(f"Nombre del Álbum: {album.get('name')}")
    print(f"Tipo de Álbum: {album.get('album_type', '').capitalize()}")
    print(f"Número de Pistas: {album.get('total_tracks')}")
    print(f"Fecha de Lanzamiento: {album.get('release_date')} (precisión: {album.get('release_date_precision')})")
    print(f"Grupo del Álbum: {album.get('album_group')}")
    
    # Información del artista
    print("\nInformación del Artista")
    artist = album.get('artists', [{}])[0]
    print(f"Nombre: {artist.get('name')}")
    print(f"URL de Spotify: {artist.get('external_urls', {}).get('spotify')}")
    
    # Enlaces externos
    print("\nEnlaces Externos")
    print(f"Spotify del Álbum: {album.get('external_urls', {}).get('spotify')}")
    
    # Imágenes del álbum
    print("\nImágenes del Álbum")
    for image in album.get('images', []):
        print(f"- {image.get('height')}x{image.get('width')} - {image.get('url')}")
    
    # Disponibilidad en mercados
    available_markets = album.get('available_markets', [])
    print("\nDisponibilidad en Mercados")
    print(f"Disponible en {len(available_markets)} países (Ejemplos: {', '.join(available_markets[:5])}, ...)")
    
    # Identificadores
    print("\nIdentificadores")
    print(f"ID del Álbum: {album.get('id')}")
    print(f"URI: {album.get('uri')}")
    print(f"Enlace API: {album.get('href')}")

