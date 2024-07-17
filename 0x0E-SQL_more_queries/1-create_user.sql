--create a user identified by the given pass and pass all privileges on the server 


CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd'; --create user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd'; -- granting privileges
FLUSH PRIVILEGES;
