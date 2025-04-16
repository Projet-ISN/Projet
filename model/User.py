from model.UserPersonalInformation import UserPersonalInformation
from model.SurveyAnswers import SurveyAnswers
from model.UserAccountInformation import UserAccountInformation


class User:
    def __init__(
        self,
        account_information: UserAccountInformation,
        personal_information: UserPersonalInformation = None,
        answers: SurveyAnswers = None,
    ):
        self.account_information = account_information
        self.personal_information = personal_information
        self.answers = answers

    def __eq__(self, other):
        if not isinstance(other, User):
            return False

        return self.account_information.username == other.account_information.username

    def __str__(self):
        return f"{self.username}"

    def __repr__(self):
        return f"User(username={self.username})"
