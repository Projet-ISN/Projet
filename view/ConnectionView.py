# -*- coding: utf-8 -*-
"""
Created on Sat Jun  7 15:38:06 2025

@author: stani
"""

import tkinter as tk
from tkinter import messagebox
from view.AccountCreationView import AccountCreationView
from view.MainView import MainView


class ConnectionView(tk.Tk):
    def __init__(self, account_controller, user_controller, window_controller):
        super().__init__()
        self.title("Interface de connexion")
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

        # Champ bienvenue
        tk.Label(
            main_frame,
            text="Bienvenue à toi jeune célibataire !",
            font=("Helvetica", 24, "bold"),
            bg="#fbe8ea",
        ).pack(pady=100)

        # Champ Username
        tk.Label(
            main_frame, text="Nom d'utilisateur :", font=font_label, bg="#fbe8ea"
        ).pack(pady=10)
        self.user_entry = tk.Entry(main_frame, font=font_entry)
        self.user_entry.pack(pady=5)

        # Champ Mot de passe
        tk.Label(main_frame, text="Mot de passe :", font=font_label, bg="#fbe8ea").pack(
            pady=10
        )
        self.password_entry = tk.Entry(main_frame, font=font_entry, show="*")
        self.password_entry.pack(pady=5)

        # Bouton Valider
        self.validate_button = tk.Button(
            main_frame,
            text="Valider",
            font=font_button,
            bg="#e1a4b6",
            fg="white",
            relief="flat",
            command=self.login,
        )

        self.validate_button.pack(pady=20)  # pady modifie

        # Frame pour les deux petits boutons
        bottom_frame = tk.Frame(main_frame, bg="#fbe8ea")
        bottom_frame.pack(pady=20)

        self.password_perdu = tk.Button(
            bottom_frame,
            text="← Mot de passe oublié ?",
            font=font_button,
            bg="#e1a4b6",
            fg="white",
            relief="flat",
            command=self.mot_de_passe_perdu,
        )
        self.password_perdu.pack(side=tk.LEFT, padx=100, pady=70)

        self.new_user = tk.Button(
            bottom_frame,
            text="Créer un nouveau compte →",
            font=font_button,
            bg="#e1a4b6",
            fg="white",
            relief="flat",
            command=self.creer_nouveau_compte,
        )

        self.new_user.pack(side=tk.RIGHT, padx=100, pady=70)

    def mot_de_passe_perdu(self):
        messagebox.showinfo(message="Dommage :(")

    def creer_nouveau_compte(self):
        account_creation_view = AccountCreationView(
            self.account_controller, self.user_controller, self.window_controller
        )
        self.window_controller.go_to_window(self, account_creation_view)

    def login(self):
        username = self.user_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
            return

        user_account = self.account_controller.get_account(username)

        if user_account is None:
            messagebox.showerror(
                "Erreur", "Nom d'utilisateur ou mot de passe incorrect."
            )
            return

        if not self.account_controller.verify_password(username, password):
            messagebox.showerror(
                "Erreur", "Nom d'utilisateur ou mot de passe incorrect."
            )
            return

        self.window_controller.go_to_window(
            self, MainView(username, self.user_controller, self.window_controller)
        )
        print(f"Connexion réussie pour l'utilisateur : {username}")
