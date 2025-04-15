from model import UserInformation
from model.SurveyAnswers import SurveyAnswers


class User:
    def __init__(
        self,
        username: str,
        password: str,
        information: UserInformation = None,
        answers: SurveyAnswers = None,
    ):
        self.username = username
        self.password = password
        self.information = information
        self.answers = answers

    def __eq__(self, other):
        if not isinstance(other, User):
            return False

        return self.username == other.username

    def __str__(self):
        return f"{self.username}"

    def __repr__(self):
        return f"User(username={self.username})"
