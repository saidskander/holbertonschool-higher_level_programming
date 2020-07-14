-- Creates the MySQL server user user_0d_1.
CREATE USER if not exist user_0d_1
BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES
    ON *.*
    TO 'user_0d_1'@'localhost';

