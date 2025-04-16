import os

from dotenv import find_dotenv, load_dotenv

from model.database.DatabaseConnector import DatabaseConnector
from model.database.AccountDAO import AccountDAO

# Load environment variables from .env file
load_dotenv(find_dotenv())


def main():
    database_connector = DatabaseConnector(
        f"{os.environ.get('DATABASE_HOST')}:{os.environ.get('DATABASE_PORT')}",
        os.environ.get("DATABASE_USER"),
        os.environ.get("DATABASE_PASSWORD"),
        os.environ.get("DATABASE_NAME"),
    )

    database = AccountDAO(database_connector)

# Rien ne doit être modifié après cette ligne
# Le code à exécuter doit être écrit dans la fonction main()
if __name__ == "__main__":
    main()
