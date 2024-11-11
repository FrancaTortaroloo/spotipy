#%%
import api_spotify_soporte as api
import requests
import json
#%%
#extraer albumes de linkin park
sp = api.credenciales()

#%%
albumes_lp = sp.artist_albums("https://open.spotify.com/intl-es/artist/6XyY86QOPPrYVGvF9ch6wz?si=UNSuzA5zRGCs5dM8NHj91A", include_groups= 'album')

#%%
print(json.dumps(albumes_lp, indent = 4))
# %%
albumes_lp.keys()
# %%
albumes_lp['items'][2]
# %%
id_album = []

for id in albumes_lp['items']:
    id_album.append([id['id']])

print(id_album)

#%%
nombre_album = []

for nombre in albumes_lp['items']:
    nombre_album.append(nombre['name'])

print(nombre_album)

# %%

cant_tracks = []

for tracks in albumes_lp['items']:
    cant_tracks.append(tracks['total_tracks'])
    
print(cant_tracks)

# %%
release_date = []

for dates in albumes_lp['items']:
    release_date.append(dates['release_date'])

print(release_date)

#%%

llamada = sp.album_tracks('494aUGKXMH5ruXtR3O1a3H',30,0)

print(llamada)

#%%
llamada['items'][0]['name']
#%%
nombre_track = []

for t_name in llamada['items']:
    nombre_track.append(t_name['name'])

print(nombre_track)


#%%

llamada['total']

#%%
stop = llamada['total']

for e in range(stop):
    print(e)
#%%

#diccionario para almacenar los id de los albumes con sus tracks

album_tracks = {}

#extraer los nombres de los tracks para cada album

for a_id in id_albums:
    a_id = a_id[0] #extrae el id del album desde la lista
    tracks = sp.album_tracks(a_id)

    #almacenar los nombres de las pistas en una lista
    tracks_names = []
    for t in tracks['items']:
        tracks_names.append(t['name'])
        
    #asocia el ID_album con los nombres de las pistas en el dicc
    album_tracks[a_id] = tracks_names

#ver el diccionario
    
print(album_tracks)
#%%
'''
#extraer de api genius

genius = "https://api.genius.com/search?q=hello&access_token=[fMasfQtTmAK7uJ4Hz7bsnHGTsFEx_qrSTO1-PdgDVmn2S0eKsMKJsXBULQiN463C]"
# %%


# Reemplaza con tu token de Genius
token = "Bearer fMasfQtTmAK7uJ4Hz7bsnHGTsFEx_qrSTO1-PdgDVmn2S0eKsMKJsXBULQiN463C"

# Configura los encabezados de autorización
headers = {
    "Authorization": token
}

# Prueba una solicitud de búsqueda para Linkin Park (por ejemplo)
url = "https://api.genius.com/search"
params = {
    "q": "Linkin Park"
}

# Haz la solicitud
response = requests.get(url, headers=headers, params=params)

# Verifica el estado de la respuesta y muestra los datos
if response.status_code == 200:
    data = response.json()
    print(data)  # Imprime los resultados de la búsqueda
else:
    print("Error:", response.status_code, response.text)

# %%
data['response']
'''

