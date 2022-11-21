import pymysql
from data_base.consts.data_base_consts import *
from data_base.consts.queries import *
from data_base.abstract_bank_dm import AbstractBankDM
from data_base.models.user import User
from data_base.models.transaction import Transaction


class DBException(Exception):
    pass


class DBNoConnection(DBException):
    pass


class DBNoData(DBException):
    pass


class Bank_DB_Manager(AbstractBankDM):
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
            self.connection.ping()
            if not self.connection.open:
                raise DBNoConnection
        except (DBNoConnection, AttributeError) as e:
            self._initialize_connection()

    def get_transactions_by_user_id(self, user_id):
        self._verify_connection()
        with self.connection.cursor() as cursor:
            cursor.execute(SELECT_ALL_TRANSACTIONS.format(user_id=user_id))
            results = cursor.fetchall()
        return [Transaction(**res) for res in results]

    def _get_category_id(self, category_name):
        self._verify_connection()
        with self.connection.cursor() as cursor:
            cursor.execute(
                SELECT_CATEGORY_ID_BY_NAME.format(name=category_name))
            result = cursor.fetchone()
            if result is None:
                raise DBNoData
            return result.get("category_id")

    def _add_new_category(self, category_name):
        self._verify_connection()
        category_name = "'" + category_name + "'"
        with self.connection.cursor() as cursor:
            cursor.execute(INSERT_INTO_CATEGORY % (category_name))
            self.connection.commit()
            return cursor.lastrowid

    def get_transaction_by_id(self, transaction_id):
        self._verify_connection()
        with self.connection.cursor() as cursor:
            cursor.execute(SELECT_TRANSACTION_BY_ID.format(
                transaction_id=transaction_id))
            return cursor.fetchone()

    def add_transaction(self, user_id, category_name, amount, vendor):
        self._verify_connection()
        try:
            category_id = self._get_category_id(category_name)
        except DBNoData:
            category_id = self._add_new_category(category_name)
        with self.connection.cursor() as cursor:
            cursor.execute(INSERT_NEW_TRANSACTION.format(
                user_id=user_id, category_id=category_id, amount=amount, vendor=vendor))
            self.connection.commit()
            return self.get_transaction_by_id(cursor.lastrowid)

    def delete_transaction(self, transaction_id):
        self._verify_connection()
        with self.connection.cursor() as cursor:
            cursor.execute(DELETE_TRANSACTION_BY_ID.format(
                transaction_id=transaction_id))
            self.connection.commit()

    def get_breakdown_by_category(self):
        self._verify_connection()
        with self.connection.cursor() as cursor:
            cursor.execute(SELECT_TRANSACTION_BREAKDOWN_BY_CATEGORY)
            return cursor.fetchall()

    def get_balance_of_user(self, user_id):
        self._verify_connection()
        with self.connection.cursor() as cursor:
            cursor.execute(GET_BALANCE_OF_USER_BY_ID.format(id=user_id))
            balance = cursor.fetchone()
        if balance is None:
            raise DBNoData(NO_USER_MESSAGE.format(user_id=user_id))
        return float(balance.get("balance"))

    def get_user_info(self, user_id):
        self._verify_connection()
        with self.connection.cursor() as cursor:
            cursor.execute(GET_USER_BY_ID.format(id=user_id))
            user_info = cursor.fetchone()
        if user_info is None:
            raise DBNoData(NO_USER_MESSAGE.format(user_id=user_id))
        return User(user_info)
    
    def set_balance_of_user(self, user_id, new_balance):
        self._verify_connection()
        with self.connection.cursor() as cursor:
            result = cursor.execute(SET_USER_BALANCE.format(id=user_id, balance=new_balance))
            self.connection.commit()
        return result

bank_db_manager = Bank_DB_Manager()
