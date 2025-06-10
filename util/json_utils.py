import json
import os

from util.appariement import Person


def load_questions(file_path: str) -> list:
    """
    Load the questions from a JSON file into a list.

    :param file_path: Path to the JSON file.
    :return: Questions as a list.
    """

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
        questions = list(data)

        return questions


def load_user_as_person(username: str) -> dict:
    """
    Load user data from a JSON file and convert it into a Person object.
    :param file_path: Path to the JSON file containing user data.
    :return: A Person object containing answers, expectations, and importances.
    """
    file_path = f"data/users/{username}.json"

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

        answers = [answer for answer in data.get("answers", {}).values()]

        answers.pop(4)

        expectations = [
            expectation["answer"]
            for expectation in data.get("expectations", {}).values()
        ]

        expectations.pop(4)
        
        importances = [
            importance["importance"]
            for importance in data.get("expectations", {}).values()
        ]

        importances.pop(4)

        print(answers, expectations, importances)

        return Person(answers, expectations, importances)

def get_usernames() -> list:
    """
    Get a list of all usernames from the user data directory.
    :return: List of usernames.
    """

    folder = "data/users"
    if not os.path.exists(folder):
        return []

    return [
        filename[:-5] for filename in os.listdir(folder) if filename.endswith(".json")
    ]  # Remove the '.json' extension