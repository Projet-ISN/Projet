import bcrypt

from model.UserAccountInformation import UserAccountInformation
from util.database import database


class AccountController:
    # C'est équivalent à un constructeur vide mais c'est plus clair.
    def __init__(self):
        pass

    def create_account(self, user_account_information: UserAccountInformation):
        # Salt and hash the password before saving it
        hashed_password = bcrypt.hashpw(
            user_account_information.password.encode('utf-8'), bcrypt.gensalt()
        )
        user_account_information.password = hashed_password.decode('utf-8')

        return database.save_account(user_account_information)

    def get_account(self, username: str):
        return database.get_account(username)

    def delete_account(self, username: str):
        return database.delete_account(username)

    def update_account(self, username: str, new_data: UserAccountInformation):
        return database.update_account(username, new_data)

    def account_exists(self, username: str):
        user = database.get_account(username)
        if user is None:
            return False
        else:
            return True
        
    def verify_password(self, username: str, password: str):
        account = database.get_account(username)
        if account is None:
            return False
        
        # Check if the provided password matches the stored hashed password
        return bcrypt.checkpw(password.encode('utf-8'), account.password.encode('utf-8'))
