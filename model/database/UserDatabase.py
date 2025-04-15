from model.database.DatabaseConnector import DatabaseConnector


class UserDatabase:
    def __init__(self, connector: DatabaseConnector):
        self.connector = connector
