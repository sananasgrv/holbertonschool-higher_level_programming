-- Creating read only user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT *.* TO 'user_0d_2'@'localhost';
