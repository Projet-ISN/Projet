import json
import os
from util.database import database

FOLDER = "data/users"
if not os.path.exists(FOLDER):
    os.mkdir(FOLDER)


class UserInformationController:
    """
    Classe pour gérer les informations personnelles des utilisateurs.
    Elle permet de créer, récupérer et supprimer les informations des utilisateurs dans des fichiers JSON.
    """
    # C'est équivalent à un constructeur vide mais c'est plus clair.
    def __init__(self):
        pass

    def create_user_information(self, username, user_data):
        file_path = f"{FOLDER}/{username}.json"
        with open(file_path, "w") as fichier:
            json.dump(user_data.to_dict(), fichier, indent=4)

    def get_user_information(self, username):
        file_path = f"{FOLDER}/{username}.json"
        try:
            with open(file_path, "r") as _:
                return True
        except FileNotFoundError:
            return False

    def delete_user_information(self, username):
        file_path = f"{FOLDER}/{username}.json"
        try:
            os.remove(file_path)
            return True
        except FileNotFoundError:
            return False
        except Exception as e:
            print(f"Erreur lors de la suppression du fichier : {e}")
            return False
