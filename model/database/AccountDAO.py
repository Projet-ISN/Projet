from model.UserAccountInformation import UserAccountInformation
from model.database.DatabaseConnector import DatabaseConnector

TABLE_NAME = "accounts"


class AccountDAO:
    """
    Cette classe gère les opérations de base de données pour les comptes utilisateurs.
    Elle permet de sauvegarder, récupérer et supprimer des comptes dans la base de données.
    Elle sert à simplifier, centraliser et rendre plus lisible les opérations liées aux comptes utilisateurs.
    """

    def __init__(self, connector: DatabaseConnector):
        self.__connector = connector

    def save_account(self, user: UserAccountInformation) -> bool:
        query = f"INSERT INTO {TABLE_NAME} (username, password) VALUES (%s, %s) ON DUPLICATE KEY UPDATE password = %s"
        params = (
            user.username,
            user.password,
            user.password,
        )

        try:
            self.__connector.execute_query(query, params)
        except Exception as e:
            print(f"Error saving account: {e}")
            return False

        return True

    def get_account(self, username: str) -> UserAccountInformation | None:
        query = f"SELECT * FROM {TABLE_NAME} WHERE username = %s"
        params = (username,)

        try:
            result = self.__connector.execute_query(query, params)
            if result:
                information = UserAccountInformation(
                    username=result[0][0],
                    password=result[0][1],
                )

                return UserAccountInformation(information)

        except Exception as e:
            print(f"Error retrieving account: {e})")

        return None

    def delete_account(self, username: str) -> bool:
        query = f"DELETE FROM {TABLE_NAME} WHERE username = %s"
        params = (username,)

        try:
            self.__connector.execute_query(query, params)
        except Exception as e:
            print(f"Error deleting account: {e}")
            return False

        return True
