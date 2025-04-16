class UserAccountInformation:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def __str__(self):
        return f"{self.username}"

    def __repr__(self):
        return f"UserAccountInformation(username={self.username})"
