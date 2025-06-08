from view.ConnectionView import ConnectionView
from controller.UserController import UserController
from controller.WindowsController import WindowsController


def main():
    user_controller = UserController()
    windows_controller = WindowsController()
    app = ConnectionView(user_controller, windows_controller)
    app.mainloop()


# Rien ne doit être modifié après cette ligne
# Le code à exécuter doit être écrit dans la fonction main()
if __name__ == "__main__":
    main()
