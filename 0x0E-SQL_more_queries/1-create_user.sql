--create a user identified by the given pass and pass all privileges on the server 


CREATE USER 
	if NOT EXISTS 'user_0d_1'@'localhost'
	IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL privileges
	ON *.* TO 'user_0d_1'@'localhost'
	IDENTIFIED BY 'user_0d_1_pwd';
FLUSH PRIVILEGES;
