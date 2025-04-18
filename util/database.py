from model.database.DatabaseConnector import DatabaseConnector
from model.database.AccountDAO import AccountDAO

import os

from dotenv import find_dotenv, load_dotenv

# Load environment variables from .env file
load_dotenv(find_dotenv())

__database_connector = DatabaseConnector(
    os.environ.get("DATABASE_HOST"),
    os.environ.get("DATABASE_USER"),
    os.environ.get("DATABASE_PASSWORD"),
    os.environ.get("DATABASE_NAME"),
)

database = AccountDAO(__database_connector)
