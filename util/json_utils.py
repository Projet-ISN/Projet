import json

from util.appariement import People


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
    
def load_user_as_people(file_path: str) -> dict:
    """
    Load user data from a JSON file into a dictionary.

    :param file_path: Path to the JSON file.
    :return: User data as a dictionary.
    """
    
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
        
        answers = [answer for answer in data.get("answers", {}).values()]
        expectations = [expectation for expectation in data.get("expectations", {}).values()["answer"]]
        importances = [importance for importance in data.get("expectations", {}).values()["importance"]]

        return People(answers, expectations, importances)
    
