from model.UserPersonalInformation import UserPersonalInformation
from model.SurveyAnswers import SurveyAnswers
from model.UserAccountInformation import UserAccountInformation


class User:
    """
    Classe représentant un utilisateur.
    Elle contient les informations de connexion, les informations personnelles et les réponses au sondage.
    """
    def __init__(
        self,
        account_information: UserAccountInformation,
        personal_information: UserPersonalInformation = None, # type: ignore
        answers: SurveyAnswers = None, # type: ignore
    ):
        self.account_information = account_information
        self.personal_information = personal_information
        self.answers = answers

    def __eq__(self, other):
        if not isinstance(other, User):
            return False

        return self.account_information.username == other.account_information.username

    def __str__(self):
        return f"{self.account_information.username}"

    def __repr__(self):
        return f"User(username={self.account_information.username})"
