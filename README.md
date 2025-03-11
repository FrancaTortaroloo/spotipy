# Proyecto: Creación de BBDD en SQL desde Python

Como una vez lo conté en mi linkedin (https://www.linkedin.com/in/franca-tortarolo/), me di cuenta que escuchar a la banda de música Linkin Park me ayuda a concentrarme a la hora de programar, hacer proyectos. Por este motivo, se me ocurrió entrar a la API de Spotify (Spotipy) para extraer toda la información sobre los álbumes y canciones de la banda antes nombrada.

Con toda la información extraída, cree 2 archivos de csv `artist_tracks.csv` y `track_features.csv`.

La extracción de datos y la creación de los csv lo hice desde Python, dentro del archivo `main.py` se procesan los datos descargados y genera archivos limpios y transformados. Lo que le da funcionalidad al archivo main.py, se encuentra dentro del archivo `api_spotify_soporte.py`.

Además, se creó una base de datos llamada `BD_linkin_park`, 2 tablas llamadas `artist_tracks` y `track_features`. Todo esto se lo realiza desde Python.


----------------------------------------------------

Project: SQL Database Creation from Python

As I once shared on my LinkedIn (https://www.linkedin.com/in/franca-tortarolo/), I realized that listening to the band Linkin Park helps me concentrate when programming and working on projects. This inspired me to explore the Spotify API (Spotipy) to extract detailed information about the band's albums and songs.

With the extracted data, I created two CSV files: `artist_tracks.csv` and `track_features.csv`.

The data extraction and CSV creation were done using Python. The `main.py` file processes the downloaded data and generates clean, transformed files. The core functionality of main.py is supported by the `api_spotify_soporte.py` file.

Additionally, I created a database named `BD_linkin_park`, along with two tables: `artist_tracks` and `track_features`. All of this was implemented using Python.
