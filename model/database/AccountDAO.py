from model.User import User
from model.UserAccountInformation import UserAccountInformation
from model.database.DatabaseConnector import DatabaseConnector


class AccountDAO:
    def __init__(self, connector: DatabaseConnector):
        self.__connector = connector

    def save_account(self, user: User) -> bool:
        query = "INSERT INTO users (username, password) VALUES (%s, %s) ON DUPLICATE KEY UPDATE password = %s"
        params = (user.account_information.username, user.account_information.password)

        try:
            self.__connector.execute_query(query, params)
        except Exception as e:
            print(f"Error saving account: {e}")
            return False

        return True

    def get_account(self, username: str) -> User:
        query = "SELECT * FROM users WHERE username = %s"
        params = (username,)

        try:
            result = self.__connector.execute_query(query, params)
            if result:
                information = UserAccountInformation(
                    username=result[0],
                    password=result[1],
                )

                return User(information)

        except Exception as e:
            print(f"Error retrieving account: {e}")

        return None

    def delete_account(self, username: str) -> bool:
        query = "DELETE FROM users WHERE username = %s"
        params = (username,)

        try:
            self.__connector.execute_query(query, params)
        except Exception as e:
            print(f"Error deleting account: {e}")
            return False

        return True
