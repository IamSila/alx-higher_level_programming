CREATE DATABASE IF NOT EXISTS hbtn_0e_usa;
USE hbtn_0e_usa;
CREATE TABLE IF NOT EXISTS states(
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
    );

INSERT INTO States (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");
