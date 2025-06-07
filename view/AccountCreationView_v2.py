# -*- coding: utf-8 -*-
"""
Created on Sat Jun  7 15:59:54 2025

@author: stani
"""

import tkinter as tk
from tkinter import messagebox
# from view.AccountCreationView import AccountCreationView

import tkinter as tk
from tkinter import messagebox
from model.User import User
from model.UserAccountInformation import UserAccountInformation
from view.AccountCreation_pt2 import CreationCompte

class AccountCreationView(tk.Tk):
    def __init__(self,user_controller,window_controller):
        super().__init__()
        self.title("Création de compte")
        self.configure(bg="#fbe8ea")
        self.attributes('-fullscreen', True)
        self.bind("<Escape>", lambda e: self.attributes("-fullscreen", False))

        self.user_controller = user_controller
        self.window_controller = window_controller

        font_label = ("Helvetica", 20)
        font_entry = ("Helvetica", 20)
        font_button = ("Helvetica", 16)

        # Frame principale
        main_frame = tk.Frame(self, bg="#fbe8ea")
        main_frame.pack(expand=True, pady=10)

        tk.Label(main_frame, text="Création de ton compte", font=("Helvetica", 24, "bold"), bg="#fbe8ea").pack(pady=100)

        # Nom d'utilisateur
        tk.Label(main_frame, text="Nom d'utilisateur :", font=font_label, bg="#fbe8ea").pack(pady=10)
        self.username_entry = tk.Entry(main_frame, font=font_entry)
        self.username_entry.pack(pady=5)

        # Mot de passe
        tk.Label(main_frame, text="Mot de passe :", font=font_label, bg="#fbe8ea").pack(pady=10)
        self.password_entry = tk.Entry(main_frame, font=font_entry, show='*')
        self.password_entry.pack(pady=5)

        # Confirmation mot de passe
        tk.Label(main_frame, text="Confirmer le mot de passe :", font=font_label, bg="#fbe8ea").pack(pady=10)
        self.password_confirm_entry = tk.Entry(main_frame, font=font_entry, show='*')
        self.password_confirm_entry.pack(pady=10)

        # Bouton de création
        self.create_account_button = tk.Button(
            main_frame,
            text="Créer un compte",
            font=font_button,
            bg="#e1a4b6",
            fg="white",
            relief="flat",
            command=self.manage_button_click
        )
        self.create_account_button.pack(pady=130)

    def manage_button_click(self):
        self.create_account()
        self.open_avatar_creation()

    def create_account(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        password_confirm = self.password_confirm_entry.get()

        if password != password_confirm:
            messagebox.showerror("Erreur", "Les mots de passe ne correspondent pas.")
            return

        user_information = UserAccountInformation(username, password)
        user = User(user_information)

        self.user_controller.create_user(user)
        print(f"Compte créé pour l'utilisateur : {username}")

    def open_avatar_creation(self):
        self.window_controller.go_to_window(self, CreationCompte(self.user_controller, self.window_controller))

# if __name__ == "__main__":
#     app = AccountCreationView()
#     app.mainloop()