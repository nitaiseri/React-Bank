import pymysql
from consts.data_base_consts import *
from consts.queries import *
import json


def create_data_base(db_name):
    try:
        initial_connection = pymysql.connect(
            host="localhost",
            user="root",
            password=""
        )
        print("creating data base...")
        initial_connection.cursor().execute(f'create database {db_name}')
        print("data base created successfully")

    except pymysql.ProgrammingError as e:
        print(e.args[1])

def create_tables():
    try:
        initial_connection = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db=DB_NAME,
        charset="utf8",
        cursorclass=pymysql.cursors.DictCursor)

        initial_connection.cursor().execute(CREATE_USER_TABLE)
        initial_connection.cursor().execute(CREATE_CATEGORY_TABLE)
        initial_connection.cursor().execute(CREATE_TRANSACTION_TABLE)
        initial_connection.commit()

        print("table created successfully")
    except Exception as e: 
        print(e.args[1])

def get_values_of_object(object):
    return [*object.values()]

def add_data_to_tables():
    try:
        initial_connection = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            db=DB_NAME,
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor
        )
        with open('backend/data_base/mock_data.json', 'r') as f:
            data = json.load(f)
            with initial_connection.cursor() as cursor:
                print("inserting values...")
                cursor.executemany(INSERT_INTO_USER, map(get_values_of_object, data["user"]))
                cursor.executemany(INSERT_INTO_CATEGORY, map(get_values_of_object, data["category"]))
                cursor.executemany(INSERT_INTO_TRANSACTION, map(get_values_of_object, data["transaction"]))
            initial_connection.commit()


            print("Done!")    
    except Exception as e: 
        print(e.args[1])
        print("coudlnt insert values!")

if __name__ == "__main__":
    # create_data_base(DB_NAME)
    # create_tables()
    add_data_to_tables()