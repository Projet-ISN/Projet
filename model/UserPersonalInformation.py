class UserPersonalInformation:
    def __init__(self, name: str, surname: str, age: int, gender: str):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender

    def __str__(self):

        info = {
            "name": self.name,
            "surname": self.surname,
            "age": self.age,
            "gender": self.gender,
        }

        return str(info)

    def __repr__(self):
        return f"UserPersonalInformation(name={self.name}, surname={self.surname}, age={self.age}, gender={self.gender})"
