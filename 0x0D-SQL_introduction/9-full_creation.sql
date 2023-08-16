-- Script that create a table in the database in your MySQL
-- server and add multiple rows.
CREATE table IF NOT EXISTS second_table(id INT, name VARCHAR(256), score INT)
INSERT INTO second_table  VALUES (1, "John", 10), (2,  "Alex", 3), (3, "Bob", 14), (4, "George", 8);
