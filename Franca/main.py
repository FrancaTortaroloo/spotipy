#%%
import api_spotify_soporte as api
import requests
import json
import mysql.connector
from mysql.connector import errorcode

#%%
#extraer albumes de linkin park
sp = api.credenciales()

#%%
albumes_lp = sp.artist_albums("https://open.spotify.com/intl-es/artist/6XyY86QOPPrYVGvF9ch6wz?si=UNSuzA5zRGCs5dM8NHj91A", include_groups= 'album')

#%%
print(json.dumps(albumes_lp, indent = 4))
# %%
dicc_lp = api.extraer_info(albumes_lp)
dicc_lp
#%%
id_albums = [['494aUGKXMH5ruXtR3O1a3H'], ['1X472EvsSqH09RyrqbtyXU'], ['3Q9wXhEAX7NYCPP0hxIuDz'], 
             ['28DUZ0itKISf2sr6hlseMy'], ['0zcNtUZ2oEpRmiDuWBFvcX'], ['5Eevxp2BCbWq25ZdiXRwYd'], 
             ['6hU9JCoqq4GjYq86dQ1o9b'], ['3XB2yloP7l00tEUmaODtVi'], ['2FUsvD1bw53HGOjAg56vRD'], 
             ['7qRKpkP0jSOlBMLYZhAMCh'], ['4XHIjbhjRmqWlosjj5rqSI'], ['0hJ3A7sih1AXDoMjXHLr7Q'], 
             ['7IYqppCBhR5z9z8JqgXuxi'], ['4flcwtqnLoKZJ2wrCp1aJq'], ['1FiRqhpAowNK8gTl5sOhxZ'], 
             ['4fy0SXW5G8evBCo2A3kn02'], ['5uvXx5ZQswNRFCdHR521YZ'], ['72seWTJF9U5SljizfyF2ZK'], 
             ['4JtIVJRA342O0YoAchen5Q'], ['7pgs38iLfEqUtwgCRgvbND']]


album_tracks = api.obtener_tracks(sp, id_albums)
album_tracks

#%%
csv = api.convertir_csv(album_tracks)
csv
#%%

csv1 = api.dicc_csv(dicc_lp)
csv1

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

