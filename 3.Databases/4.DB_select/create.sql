create table if not exists genre (
	id serial primary key,
	name varchar(80) not null unique
);

create table if not exists artist (
	id serial primary key,
	artist_name varchar(100) not null
);


create table if not exists genreartist(
	id serial primary key,
	artist_id integer not null references artist(id),
	genre_id integer not null references genre(id)
);

create table if not exists album (
	id serial primary key,
	album_name varchar(100) not null,
	album_date date not null
);

create table if not exists albumartist (
	id  serial primary key,
	album_id integer not null references album(id),
	artist_id integer not null references artist(id)
);

create table if not exists track (
	id serial primary key,
	track_name varchar(100) not null,
	track_duration numeric(3,2) not null,
	album_id integer references album(id) 
);

create table if not exists collection(
	id serial primary key,
	collection_name varchar(100) not null,
	collection_date date not null
);

create table if not exists collectiontrackalbum(
	id serial primary key,
	collection_id integer not null references collection(id),
	album_id integer not null references album(id),
	track_id integer not null references track(id)
);