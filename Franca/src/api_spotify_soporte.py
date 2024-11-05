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
    

url_playlist = "https://open.spotify.com/intl-es/album/6PFPjumGRpZnBzqnDci6qJ?si=iqQRrwOpSz2I7JeKbwuS2g"
#print(url_playlist.split("/")[-1].split("?")[0])

def preparamos_url(link):
    return link.split("/"[-1].split("?")[0])

prueba = preparamos_url(url_playlist)
print(prueba)