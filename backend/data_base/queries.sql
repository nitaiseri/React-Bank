use bank_app;

drop table transaction;
drop table category;
drop table user;


-- CREATE TABLE category(
--     category_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
--     name VARCHAR(20)
-- );

-- CREATE TABLE user(
--     user_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
--     name VARCHAR(20)
-- );

-- CREATE TABLE transaction(
--     transaction_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
--     category_id INT,
--     user_id INT,
--     amount FLOAT,
--     vendor VARCHAR(30), 
--     FOREIGN KEY(category_id) REFERENCES category(category_id),
--     FOREIGN KEY(user_id) REFERENCES user(user_id)
-- );
