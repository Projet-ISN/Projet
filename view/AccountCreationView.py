import tkinter as tk
from tkinter import messagebox

from controller.AccountController import AccountController
from controller.UserController import UserController
from controller.WindowController import WindowController
from model.UserAccountInformation import UserAccountInformation
from view.UserCreationView import UserCreationView


class AccountCreationView(tk.Toplevel):
    def __init__(
        self,
        account_controller: AccountController,
        user_controller: UserController,
        window_controller: WindowController,
    ):
        super().__init__()
        self.title("Création de compte")
        self.configure(bg="#fbe8ea")
        self.attributes("-fullscreen", True)
        self.bind("<Escape>", lambda e: self.attributes("-fullscreen", False))

        self.account_controller = account_controller
        self.user_controller = user_controller
        self.window_controller = window_controller

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        font_title = ("Helvetica", int(screen_height * 0.035), "bold")
        font_label = ("Helvetica", int(screen_height * 0.025))
        font_entry = ("Helvetica", int(screen_height * 0.025))
        font_button = ("Helvetica", int(screen_height * 0.02))

        # Frame principale
        main_frame = tk.Frame(self, bg="#fbe8ea")
        main_frame.pack(expand=True)

        tk.Label(
            main_frame,
            text="Création de ton compte",
            font=font_title,
            bg="#fbe8ea",
        ).pack(pady=(int(screen_height * 0.05), int(screen_height * 0.03)))

        # Nom d'utilisateur
        tk.Label(
            main_frame, text="Nom d'utilisateur :", font=font_label, bg="#fbe8ea"
        ).pack(pady=(10, 5))
        self.username_entry = tk.Entry(main_frame, font=font_entry, width=30)
        self.username_entry.pack(pady=5)

        # Mot de passe
        tk.Label(main_frame, text="Mot de passe :", font=font_label, bg="#fbe8ea").pack(
            pady=(10, 5)
        )
        self.password_entry = tk.Entry(main_frame, font=font_entry, show="*", width=30)
        self.password_entry.pack(pady=5)

        # Confirmation mot de passe
        tk.Label(
            main_frame,
            text="Confirmer le mot de passe :",
            font=font_label,
            bg="#fbe8ea",
        ).pack(pady=(10, 5))
        self.password_confirm_entry = tk.Entry(
            main_frame, font=font_entry, show="*", width=30
        )
        self.password_confirm_entry.pack(pady=(5, 20))

        # Bouton de création
        self.create_account_button = tk.Button(
            main_frame,
            text="Créer un compte",
            font=font_button,
            bg="#e1a4b6",
            fg="white",
            relief="flat",
            command=self.manage_button_click,
        )
        self.create_account_button.pack(
            pady=(10, int(screen_height * 0.04)), ipadx=10, ipady=5
        )

    def manage_button_click(self):
        success = self.create_account()
        if not success:
            return
        self.open_user_pt2_creation(self.username_entry.get())

    def create_account(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        password_confirm = self.password_confirm_entry.get()

        if not username or not password or not password_confirm:
            messagebox.showerror("Erreur", "Tous les champs doivent être remplis.")
            return False

        if password != password_confirm:
            messagebox.showerror("Erreur", "Les mots de passe ne correspondent pas.")
            return False

        if self.account_controller.account_exists(username):
            messagebox.showerror(
                "Erreur", "Un compte avec ce nom d'utilisateur existe déjà."
            )
            return False

        account_information = UserAccountInformation(username, password)
        self.account_controller.create_account(account_information)
        print(f"Compte créé pour l'utilisateur : {username}")
        return True

    def open_user_pt2_creation(self, username):
        self.window_controller.go_to_window(
            self,
            UserCreationView(self.user_controller, self.window_controller, username),
        )
