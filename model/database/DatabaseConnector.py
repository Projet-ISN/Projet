import mysql.connector as mysql


class DatabaseConnector:
    """
    Cette classe gère la connexion à la base de données MySQL.
    Elle permet de se connecter à la base de données, et d'exécuter des requêtes SQL.
    """

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

            return connection

        except mysql.Error as err:
            print(f"Error: {err}")
            return None

    def close_connection(self, connection):
        if connection.is_connected():
            connection.close()

    def execute_query(self, query, params=None):
        connection = self.connect()
        cursor = None

        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute(query, params)
                if not cursor.with_rows:
                    connection.commit()

                return cursor.fetchall()

            except mysql.Error as err:
                print(f"Error: {err}")

            finally:
                if cursor:
                    cursor.fetchall()
                    cursor.close()

                self.close_connection(connection)
        else:
            print("Failed to connect to the database. Query not executed.")
