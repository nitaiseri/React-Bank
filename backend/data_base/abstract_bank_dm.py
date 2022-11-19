from abc import ABC, abstractmethod

class AbstractBankDM(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_transactions_by_user_id(self, user_id):
        pass

    @abstractmethod
    def get_transaction_by_id(self, transaction_id):
        pass

    @abstractmethod
    def add_transaction(self, user_id, category_name, amount, vendor):
        pass

    @abstractmethod
    def delete_transaction(self, transaction_id):
        pass

    @abstractmethod
    def get_breakdown_by_category(self):
        pass
