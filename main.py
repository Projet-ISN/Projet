from controller.UserController import UserController
from view.ConnectionView import ConnectionView
from controller.AccountController import AccountController
from controller.WindowController import WindowController


def main():
    account_controller = AccountController()
    user_controller = UserController()
    windows_controller = WindowController()

    app = ConnectionView(account_controller, user_controller, windows_controller)
    app.mainloop()


# Rien ne doit être modifié après cette ligne
# Le code à exécuter doit être écrit dans la fonction main()
if __name__ == "__main__":
    main()
