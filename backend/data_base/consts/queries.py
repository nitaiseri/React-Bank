CREATE_CATEGORY_TABLE = "CREATE TABLE category(\
    category_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,\
    name VARCHAR(20)\
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
INSERT_INTO_TRANSACTION = "INSERT INTO transaction(category_id, user_id, amount, vendor) values (%s, %s, %s, %s)"

