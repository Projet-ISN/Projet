import json
import os
from util.database import database

FOLDER = "data/users"
if not os.path.exists(FOLDER):
    os.mkdir(FOLDER)


class UserController:
    """
    Classe pour gérer les informations personnelles des utilisateurs.
    Elle permet de créer, récupérer et supprimer les informations des utilisateurs dans des fichiers JSON.
    """

    # C'est équivalent à un constructeur vide mais c'est plus clair.
    def __init__(self):
        pass

    def create_user(self, username, user_data):
        file_path = f"{FOLDER}/{username}.json"
        with open(file_path, "w") as fichier:
            data = user_data.to_dict()
            data["username"] = username

            json.dump(data, fichier, indent=4)

    def get_user(self, username):
        file_path = f"{FOLDER}/{username}.json"
        try:
            with open(file_path, "r") as _:
                return True
        except FileNotFoundError:
            return False

    def delete_user(self, username):
        file_path = f"{FOLDER}/{username}.json"
        try:
            os.remove(file_path)
            return True
        except FileNotFoundError:
            return False
        except Exception as e:
            print(f"Erreur lors de la suppression du fichier : {e}")
            return False

    def add_users_survey_answers(self, survey_answers):
        file_path = f"{FOLDER}/{survey_answers.username}.json"
        with open(file_path, "r") as fichier:
            data = json.load(fichier)

        data["answers"] = survey_answers.answers

        with open(file_path, "w") as fichier:
            json.dump(data, fichier, indent=4)

    
    def add_users_expectations(self, expectations):
        file_path = f"{FOLDER}/{expectations.username}.json"
        with open(file_path, "r") as fichier:
            data = json.load(fichier)

        data["expectations"] = expectations.answers

        with open(file_path, "w") as fichier:
            json.dump(data, fichier, indent=4)
