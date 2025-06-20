class SurveyAnswers:
    """
    Classe représentant les réponses d'un utilisateur à un sondage.
    Elle contient le nom d'utilisateur et un dictionnaire de réponses.
    """
    def __init__(self, username: str, answers: dict):
        self.username = username
        self.answers = answers

    def __repr__(self):
        return f"SurveyAnswers(username={self.username})"