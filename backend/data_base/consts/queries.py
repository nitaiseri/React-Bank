CREATE_CATEGORY_TABLE = "CREATE TABLE category(\
    category_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,\
    name VARCHAR(20) UNIQUE\
);"

CREATE_USER_TABLE = "CREATE TABLE user(\
    user_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,\
    name VARCHAR(20),\
    balance float\
);"

CREATE_TRANSACTION_TABLE = "CREATE TABLE transaction(\
    transaction_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,\
    user_id INT,\
    category_id INT,\
    amount FLOAT,\
    vendor VARCHAR(30),\
    FOREIGN KEY(category_id) REFERENCES category(category_id),\
    FOREIGN KEY(user_id) REFERENCES user(user_id)\
);"

INSERT_INTO_USER = "INSERT INTO user(name, balance) values (%s, %s)"
INSERT_INTO_CATEGORY = "INSERT INTO category(name) values (%s)"
INSERT_INTO_TRANSACTION = "INSERT INTO transaction(user_id, category_id, amount, vendor) values (%s, %s, %s, %s)"

INSERT_NEW_TRANSACTION = "INSERT INTO transaction(user_id, category_id, amount, vendor) values ({user_id}, {category_id}, {amount}, '{vendor}')"

SELECT_ALL_TRANSACTIONS = "SELECT * FROM transaction WHERE user_id={user_id}"

SELECT_TRANSACTION_BY_ID = "SELECT * FROM transaction WHERE transaction_id={transaction_id}"

SELECT_CATEGORY_ID_BY_NAME = "SELECT category_id FROM category WHERE name='{name}'"

DELETE_TRANSACTION_BY_ID = "DELETE FROM transaction WHERE transaction_id={transaction_id}"

SELECT_TRANSACTION_BREAKDOWN_BY_CATEGORY = "SELECT name, sum\
            FROM(SELECT category_id as c_id, SUM(amount) as sum FROM transaction GROUP BY category_id) as c_s JOIN\
            category as c\
            WHERE category_id = c_id"
