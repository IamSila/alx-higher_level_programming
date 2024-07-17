-- create database ** and create a user if not exists
-- grant select privileges on user **
CREATE DATABASE
	IF NOT EXISTS `hbtn_0d_2`;
CREATE USER 
	IF NOT EXISTS 'user_0d_2'@'localhost'
	IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT
	0N 'hbtn_0d_2'.*
	TO 'user_0d_2'@'localhost'
	IDENTIFIED BY 'user_0d_2_pwd';
FLUSH PRIVILEGES;
