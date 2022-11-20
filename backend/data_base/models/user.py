class User:

    def __init__(self, user_object) -> None:
        self.id = user_object["user_id"]
        self.name = user_object["name"]
        self.balance = user_object["balance"]