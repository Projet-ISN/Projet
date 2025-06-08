# -*- coding: utf-8 -*-
"""
Created on Sat Jun  7 15:59:54 2025

@author: stani
"""

import tkinter as tk
from tkinter import messagebox

# from view.AccountCreationView import AccountCreationView

from controller.AccountController import AccountController
from controller.UserInformationController import UserInformationController
from controller.WindowController import WindowController
from model.User import User
from model.UserAccountInformation import UserAccountInformation
from view.UserCreationView import UserCreationView


class AccountCreationView(tk.Toplevel):
    def __init__(
        self,
        account_controller: AccountController,
        user_controller: UserInformationController,
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

        font_label = ("Helvetica", 20)
        font_entry = ("Helvetica", 20)
        font_button = ("Helvetica", 16)

        # Frame principale
        main_frame = tk.Frame(self, bg="#fbe8ea")
        main_frame.pack(expand=True, pady=10)

        tk.Label(
            main_frame,
            text="Création de ton compte",
            font=("Helvetica", 24, "bold"),
            bg="#fbe8ea",
        ).pack(pady=100)

        # Nom d'utilisateur
        tk.Label(
            main_frame, text="Nom d'utilisateur :", font=font_label, bg="#fbe8ea"
        ).pack(pady=10)
        self.username_entry = tk.Entry(main_frame, font=font_entry)
        self.username_entry.pack(pady=5)

        # Mot de passe
        tk.Label(main_frame, text="Mot de passe :", font=font_label, bg="#fbe8ea").pack(
            pady=10
        )
        self.password_entry = tk.Entry(main_frame, font=font_entry, show="*")
        self.password_entry.pack(pady=5)

        # Confirmation mot de passe
        tk.Label(
            main_frame,
            text="Confirmer le mot de passe :",
            font=font_label,
            bg="#fbe8ea",
        ).pack(pady=10)
        self.password_confirm_entry = tk.Entry(main_frame, font=font_entry, show="*")
        self.password_confirm_entry.pack(pady=10)

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
        self.create_account_button.pack(pady=60)

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
            messagebox.showerror("Erreur", "Un compte avec ce nom d'utilisateur existe déjà.")
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


# if __name__ == "__main__":
#     app = AccountCreationView()
#     app.mainloop()
