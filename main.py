from model.User import User
from model.UserAccountInformation import UserAccountInformation
from model.UserPersonalInformation import UserPersonalInformation
from util.database import database


def main():
    user_information = UserAccountInformation("davipccunha", "password123")
    user_personal_information = UserPersonalInformation("Davi", "Cunha", 20, "M")

    user = User(user_information, user_personal_information)

    database.save_account(user)
    retrieved_user = database.get_account(user_information.username)
    print(f"Retrieved user: {retrieved_user.account_information.username}")
    print(f"Retrieved password: {retrieved_user.account_information.password}")

    print(database.delete_account(user_information.username))
    print(f"Deleted account for user: {user_information.username}")

    retrieved_user = database.get_account(user_information.username)
    print(retrieved_user)


# Rien ne doit être modifié après cette ligne
# Le code à exécuter doit être écrit dans la fonction main()
if __name__ == "__main__":
    main()
