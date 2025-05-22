from util.database import database


class UserController:
    def __init__(self):
        pass

    def create_user(self, user_data):
        return database.save_account(user_data)

    def get_user(self, username):
        return database.get_account(username)

    def delete_user(self, username):
        return database.delete_account(username)

    def update_user(self, username, new_data):
        return database.update_account(username, new_data)
    
    def user_exists(self, username):
        user = database.get_account(username)
        if user is None:
            return False
        else:
            return True
