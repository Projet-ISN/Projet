import json


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
