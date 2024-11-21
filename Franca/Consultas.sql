#Encontrar las canciones más bailables (danceability > 0.8)
USE BD_linkin_park;

SELECT 
track_features.track_name,
track_features.danceability,
artist_tracks.album
FROM track_features
JOIN artist_tracks
ON artist_tracks.track_id = track_features.track_id
WHERE track_features.danceability > 0.8
ORDER BY track_features.danceability DESC;

#cantidad de canciones por álbum

SELECT artist_tracks.album,
COUNT(artist_tracks.track_id) AS total_tracks
FROM artist_tracks
GROUP BY artist_tracks.album
ORDER BY total_tracks DESC;


#duración promedio de las canciones
SELECT AVG(duration_ms) AS promedio_duracion_canciones
FROM track_features
ORDER BY promedio_duracion_canciones DESC;


#5 canciones más largas

SELECT 
track_features.track_name, 
track_features.duration_ms,
artist_tracks.album
FROM track_features
JOIN artist_tracks
ON track_features.track_id = artist_tracks.track_id
ORDER BY duration_ms DESC
LIMIT 5; 


#canción más melancólica

SELECT 
track_features.track_name, 
track_features.artist, 
track_features.valence,
artist_tracks.album
FROM track_features 
JOIN artist_tracks
ON track_features.track_id = artist_tracks.track_id
ORDER BY valence ASC
LIMIT 1;
