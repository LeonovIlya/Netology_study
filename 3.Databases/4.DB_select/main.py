import sqlalchemy
import psycopg2
from pprint import pprint

engine = sqlalchemy.create_engine('postgresql://postgres:postgres@localhost:5432/music')
pprint(engine)
connection = engine.connect()
print(connection)
print()

select_1 = connection.execute('''SELECT album_name, album_date FROM album
WHERE album_date BETWEEN '2018-01-01' AND '2018-12-31';
''').fetchall()
print('1.Название и год выхода альбомов, вышедших в 2018 году')
pprint(select_1)
print()

select_2 = connection.execute('''SELECT track_name, track_duration FROM track
ORDER BY track_duration DESC;
''').fetchone()
print('2.Название и продолжительность самого длительного трека')
pprint(select_2)
print()

select_3 = connection.execute('''SELECT track_name FROM track
WHERE track_duration >= 03.50;
''').fetchall()
print('3.Название треков, продолжительность которых не менее 3,5 минуты')
pprint(select_3)
print()

select_4 = connection.execute('''SELECT collection_name FROM collection
WHERE collection_date BETWEEN '2018-01-01' AND '2020-12-31';
''').fetchall()
print('4.Названия сборников, вышедших в период с 2018 по 2020 год включительно')
pprint(select_4)
print()

select_5 = connection.execute('''SELECT artist_name FROM artist
WHERE artist_name NOT LIKE '%% %%';
''').fetchall()
print('5.Исполнители, чье имя состоит из 1 слова')
pprint(select_5)
print()


select_6 = connection.execute('''SELECT track_name FROM track
WHERE track_name LIKE '%%my%%';
''').fetchall()
print('6.Название треков, которые содержат слово "мой"/"my"')
pprint(select_6)
