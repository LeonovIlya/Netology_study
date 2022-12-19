import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine('postgresql://postgres:postgres@localhost:5432/music')
pprint(engine)
connection = engine.connect()
print(connection)
print()

count_artists = connection.execute('''
    SELECT T.name, count(GA.artist_id)
    FROM genre T
    JOIN  genreartist GA ON T.id = GA.genre_id
    GROUP BY T.name
    ORDER BY count(GA.artist_id)
    ''').fetchall()
pprint(f'Количество исполнителей в каждом жанре: {count_artists}')
print()

count_track_19_20 = connection.execute('''
    SELECT a.album_name, a.album_date, count(T.id)
    FROM album a
    JOIN track T ON a.id = T.album_id
    WHERE a.album_date BETWEEN '2019-01-01' AND '2020-12-31'
    GROUP BY a.album_name, a.album_date
    ''').fetchall()
pprint(f'Количество треков, вошедших в альбомы 2019-2020 годов;: {count_track_19_20}')
print()

duration_track_average = connection.execute('''
    SELECT  A.album_name, round(AVG(T.track_duration), 2)
    FROM album A
    JOIN track T ON a.id = T.album_id
    GROUP BY A.album_name
    ORDER BY A.album_name
    ''').fetchall()
pprint(f'Cредняя продолжительность треков по каждому альбому: {duration_track_average}')
print()

album_not_in_20 = connection.execute('''
    SELECT AR.artist_name, AL.album_date
    FROM artist AR
    JOIN albumartist AA ON AR.id = AA.artist_id
    JOIN album AL ON AA.album_id = AL.id
    WHERE AL.album_date::text NOT LIKE '2020%%'
    ORDER BY AR.artist_name
    ''').fetchall()
pprint(f'Все исполнители, которые не выпустили альбомы в 2020 году: {album_not_in_20}')
print()

name_in_collection = connection.execute('''
    SELECT DISTINCT C.collection_name
    FROM collection C
    JOIN collectiontrackalbum CTA ON C.id = CTA.collection_id
    JOIN track T ON CTA.track_id = T.id
    JOIN album A ON T.album_id = A.id
    JOIN albumartist AA ON A.id = AA.album_id
    JOIN artist AR ON AA.artist_id = AR.id
    WHERE AR.artist_name LIKE 'artist_5'
    ''').fetchall()
pprint(f'Названия сборников, в которых присутствует конкретный исполнитель ("artist_5"): {name_in_collection}')
print()

album_many_genres = connection.execute('''
     SELECT AL.album_name
     FROM album AL
     JOIN albumartist AA ON AL.id = AA.album_id
     JOIN artist AR ON AA.artist_id = AR.id
     JOIN genreartist GA ON AR.id = GA.artist_id
     GROUP BY AR.artist_name, AL.album_name
     HAVING count(GA.genre_id) > 1
    ''').fetchall()
pprint(f'Название альбомов, в которых присутствуют исполнители более 1 жанра: {album_many_genres}')
print()

single_track = connection.execute('''
    SELECT T.track_name
    FROM track T
    LEFT JOIN collectiontrackalbum CTA ON T.id = CTA.track_id
    where CTA.track_id IS NULL
    ''').fetchall()
pprint(f'Наименование треков, которые не входят в сборники: {single_track}')
print()

short_track = connection.execute('''
    SELECT AR.artist_name, T.track_duration
    FROM artist AR
    JOIN albumartist AA ON AR.id = AA.artist_id
    JOIN album AL ON AA.album_id = AL.id
    JOIN track T ON AL.id = T.album_id
    WHERE T.track_duration IN (SELECT MIN(track_duration) FROM track)
    ''').fetchall()
pprint(f'Исполнителя(-ей), написавшего самый короткий по продолжительности трек : {short_track}')
print()

short_album = connection.execute('''
    SELECT AL.album_name, count(T.id)
    FROM album AL
    JOIN track T  ON AL.id = T.album_id
    GROUP BY AL.album_name 
    HAVING count(T.id) in (
        SELECT count(T.id)
        FROM album AL
        JOIN track T  ON AL.id = T.album_id
        GROUP BY AL.album_name
        ORDER BY count(T.id)
        LIMIT 1)
    ''').fetchall()
pprint(f'Название альбомов, содержащих наименьшее количество треков : {short_album}')