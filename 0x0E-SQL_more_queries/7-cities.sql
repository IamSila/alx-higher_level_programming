-- script that creates the database hbtn_0d_usa and the table cities
-- id INT unique, auto generated, can’t be null and is a primary key
-- state_id INT, can’t be null and must be a FOREIGN KEY that references to id of the states table
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(id INT AUTO_INCREMENT NOT NULL PRIMARY KEY, state_id INT NOT NULL, CONSTRAINT FOREIGN KEY(state_id) REFERENCES states(id), name VARCHAR(256) NOT NULL)
