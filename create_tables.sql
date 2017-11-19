\c postgres;
drop database if exists ellomix;
create database ellomix;
\c ellomix;

create table Users(
	user_id serial primary key not null unique,
	name varchar(75) not null,
	description varchar(500),
	followers_count int,
	following_count int,
	photo_url text
);

create table Track(
	track_id serial primary key not null unique,
	artist varchar(75),
	title text,
	stream_url text,
	artwork_url text,
	source text
);

create table Playlist(
	playlist_id serial primary key not null unique,
	track_id serial references Track(track_id)
);

create table TimelinePost(
	post_id serial primary key not null unique,
	user_id serial references Users(user_id),
	track_id serial references Track(track_id),
	date_posted timestamp with time zone,
	description text
);

create table Comment(
	user_id serial references Users(user_id),
	comment varchar(500)
);

create table Relationship(
	follower_id serial primary key not null unique,
	user_id serial references Users(user_id)
);

create table Message(
	message_id serial primary key not null unique,
	message text,
	user_id serial references Users(user_id),
	photo_url text
);

create table Chat(
	chat_id serial primary key not null unique,
	from_recipent serial,
	most_recent_message text,
	playlist_id serial references Playlist(playlist_id),
	message_id serial references Message(message_id)
);

create table Chat_Users(
	chat_user_id serial primary key not null unique,
	user_id serial references Users(user_id),
	chat_id serial references Chat(chat_id)
);
