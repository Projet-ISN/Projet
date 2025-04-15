class SurveyAnswers:
    def __init__(self, username: str, answers: dict):
        self.username = username
        self.answers = answers

    def __repr__(self):
        return f"SurveyAnswers(username={self.username})"