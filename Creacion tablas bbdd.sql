CREATE TABLE artist_tracks (
	track_id VARCHAR(255) PRIMARY KEY,
    album VARCHAR (255),
    album_release_date DATE,
    track_name VARCHAR(255)    
);

CREATE TABLE track_features (
	track_id VARCHAR(255),
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
);
    
    