#Encontrar las canciones más bailables (danceability > 0.8)

SELECT track_features.track_name,
track_features.danceability
FROM track_features
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

SELECT track_name, duration_ms
FROM track_features
ORDER BY duration_ms DESC
LIMIT 5; 


#canción más melancólica

SELECT track_name, artist, valence
FROM track_features 
ORDER BY valence ASC
LIMIT 1;
