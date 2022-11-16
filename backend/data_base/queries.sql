use bank_app;

-- drop table transaction;
-- drop table category;
-- drop table user;


-- CREATE TABLE category(
--     category_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
--     name VARCHAR(20) UNIQUE
-- );

-- CREATE TABLE user(
--     user_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
--     name VARCHAR(20),
--     balance float
-- );

-- CREATE TABLE transaction(
--     transaction_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
--     user_id INT,
--     category_id INT,
--     amount FLOAT,
--     vendor VARCHAR(30), 
--     FOREIGN KEY(category_id) REFERENCES category(category_id),
--     FOREIGN KEY(user_id) REFERENCES user(user_id)
-- );

-- SELECT name, sum
-- FROM(SELECT category_id as c_id, SUM(amount) as sum FROM transaction GROUP BY category_id) as c_s JOIN
-- category as c
-- WHERE category_id = c_id
