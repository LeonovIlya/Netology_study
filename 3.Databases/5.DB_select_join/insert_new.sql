INSERT INTO
	genreartist(id, artist_id, genre_id)
VALUES
	(1, 1, 1),
	(2, 2, 1),
	(3, 3, 1),
    (4, 4, 1),
    (5, 5, 1),
    (6, 6, 2),
    (7, 7, 2),
    (8, 8, 2),
    (9, 9, 2),
    (10, 10, 3),
    (11, 11, 3),
    (12, 12, 3),
    (13, 13, 4),
    (14, 14, 4),
    (15, 15, 5);

DELETE FROM track;

INSERT INTO
	track(id, track_name, track_duration, album_id)
VALUES
    (1, 'track_1', 3.05, 1),
    (2, 'track_2', 3.10, 2),
    (3, 'track_3', 4.15, 3),
    (4, 'track_4', 3.15, 4),
    (5, 'track_5', 4.25, 5),
    (6, 'track_6', 5.05, 6),
    (7, 'track_7', 2.50, 7),
    (8, 'track_8', 4.00, 8),
    (9, 'track_9', 5.50, 1),
    (10, 'track_10', 2.30, 2),
    (11, 'track_11', 1.55, 3),
    (12, 'track_12', 4.40, 4),
    (13, 'track_13', 5.20, 5),
    (14, 'track_14', 2.45, 6),
    (15, 'my_14', 2.45, 7),
    (16, 'my', 1.45, 8);

INSERT INTO
	albumartist (id, album_id, artist_id  )
VALUES
    (1, 1, 1),
    (2, 2, 2),
    (3, 3, 3),
    (4, 4, 4),
    (5, 5, 5),
    (6, 6, 6),
    (7, 7, 7),
    (8, 8, 8);

INSERT INTO
	collectiontrackalbum  (id, collection_id, album_id, track_id)
VALUES
    (1, 1, 1, 1),
    (2, 2, 2, 2),
    (3, 3, 3, 3),
    (4, 4, 4, 4),
    (5, 5, 5, 5),
    (6, 6, 6, 6),
    (7, 7, 7, 7),
    (8, 8, 8, 8);
   
INSERT INTO
	genreartist(id, artist_id, genre_id)
VALUES
	(16, 1, 2),
	(17, 1, 3),
	(18, 1, 4);

