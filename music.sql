
DROP DATABASE IF EXISTS 'Music';

CREATE DATABASE 'Music';
USE 'MUSIC';


DROP TABLE IF EXISTS 'artist';
DROP TABLE IF EXISTS 'album';
DROP TABLE IF EXISTS 'song';

CREATE TABLE 'artist'
(
    'Artist_ID' INT NOT NULL,
    'Name' VARCHAR(130) NOT NULL
);

CREATE TABLE 'album'
(
    'Track_ID' INT NOT NULL,
    'Name' VARCHAR(200) NOT NULL,
    'Album_ID' INT NOT NULL
);

CREATE TABLE 'song'
(
    'Song_ID' INT NOT NULL,
    'Song_Name' VARCHAR(200) NOT NULL,
    'Album_ID' INT NOT NULL,
    'Time' INT NOT NULL
);
