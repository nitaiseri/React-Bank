import pymysql
from consts.data_base_consts import *
from consts.queries import *

class DBException(Exception):
    pass

class DBNoConnection(DBException):
    pass

class Bank_DB_Manager:
    def __init__(self):
        self.connection = None
        self._initialize_connection()

    def _initialize_connection(self):
        self.connection = pymysql.connect(
            host=HOST,
            user=USER,
            password=PWD,
            db=DB_NAME,
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor)
    
    def _verify_connection(self):
        try:
            if not self.connection.open:
                raise DBNoConnection
        except (DBNoConnection, AttributeError) as e:
            self._initialize_connection()

    def get_transactions(self):
        self._verify_connection()
        with self.connection.cursor() as cursor:
            cursor.execute(SELECT_ALL_TRANSACTIONS)
            return cursor.fetchall()

        
db_manager = Bank_DB_Manager()
print(db_manager.get_transactions())

