class UserInformation:
    def __init__(self, name: str, surname: str, age: int, gender: str):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender

    def __repr__(self):
        return f"UserInformation({self.name=}, {self.surname=}, {self.age=}, {self.gender=})"
