import mysql.connector as mysql


class DatabaseConnector:
    def __init__(self, host: str, user: str, password: str, database: str):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        try:
            connection = mysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
            )

            if connection.is_connected():
                print("Connection established")

            return connection

        except mysql.Error as err:
            print(f"Error: {err}")
            return None

    def close_connection(self, connection):
        if connection.is_connected():
            connection.close()

            print("Connection closed.")

    def execute_query(self, query, params=None):
        connection = self.connect()
        cursor = None

        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute(query, params)
                connection.commit()

            except mysql.Error as err:
                print(f"Error: {err}")

            finally:
                if cursor:
                    cursor.close()

                self.close_connection(connection)
        else:
            print("Failed to connect to the database. Query not executed.")
