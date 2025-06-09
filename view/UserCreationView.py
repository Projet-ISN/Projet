# -*- coding: utf-8 -*-
"""
Created on Thu Jun  5 08:34:12 2025

@author: stani
"""

import tkinter as tk
from controller.UserController import UserController
from controller.WindowController import WindowController
from model.UserPersonalInformation import UserPersonalInformation
from view.AvatarCreationView import AvatarCreationView
from view.QuestionsView import QuestionsView


class UserCreationView(tk.Toplevel):
    def __init__(
        self,
        user_controller: UserController,
        window_controller: WindowController,
        username,
    ):
        super().__init__()

        self.title("Création de ton compte")
        self.geometry("800x600")
        self.configure(bg="#fbe8ea")
        self.attributes("-fullscreen", True)
        self.bind("<Escape>", lambda e: self.attributes("-fullscreen", False))

        self.user_controller = user_controller
        self.window_controller = window_controller
        self.username = username

        # Style général
        font_label = ("Helvetica", 20)
        font_entry = ("Helvetica", 20)
        font_button = ("Helvetica", 16)

        self.frame_gen = tk.Frame(self, bg="#fbe8ea")
        self.frame_gen.pack(pady=40)

        self.prenom = tk.Label(
            self.frame_gen,
            text="Donne nous tes petites informations !",
            font=("Helvetica", 24, "bold"),
            bg="#fbe8ea",
        )
        self.prenom.pack(pady=40)
        # Prénom
        self.prenom = tk.Label(
            self.frame_gen, text="Prénom :", font=font_label, bg="#fbe8ea"
        )
        self.prenom.pack(pady=5)
        self.entry1 = tk.Entry(self.frame_gen, font=font_entry, justify="center")
        self.entry1.pack(pady=20)

        # Nom
        self.nom = tk.Label(self.frame_gen, text="Nom :", font=font_label, bg="#fbe8ea")
        self.nom.pack(pady=5)
        self.entry2 = tk.Entry(self.frame_gen, font=font_entry, justify="center")
        self.entry2.pack(pady=10)

        # Âge
        self.age_value = tk.IntVar(value=18)
        self.text1 = tk.Label(
            self.frame_gen, text="Âge :", font=font_label, bg="#fbe8ea"
        )
        self.text1.pack(pady=10)
        self.scale = tk.Scale(
            self.frame_gen,
            from_=18,
            to=99,
            variable=self.age_value,
            orient=tk.HORIZONTAL,
            font=("Helvetica", 16),
            bg="#fbe8ea",
            length=400,
        )
        self.scale.pack(pady=10)

        # Genre
        self.text2 = tk.Label(
            self.frame_gen, text="Genre :", font=font_label, bg="#fbe8ea"
        )
        self.text2.pack(pady=10)

        self.choix = tk.StringVar(value="Non renseigné")
        self.option1 = tk.Radiobutton(
            self.frame_gen,
            text="Homme",
            variable=self.choix,
            value="Homme",
            font=font_label,
            bg="#fbe8ea",
            anchor="w",
            justify="center",
        )
        self.option1.pack(pady=5)
        self.option2 = tk.Radiobutton(
            self.frame_gen,
            text="Femme",
            variable=self.choix,
            value="Femme",
            font=font_label,
            bg="#fbe8ea",
            anchor="w",
            justify="center",
        )
        self.option2.pack(pady=5)
        self.option3 = tk.Radiobutton(
            self.frame_gen,
            text="Autre",
            variable=self.choix,
            value="Autre",
            font=font_label,
            bg="#fbe8ea",
            anchor="w",
            justify="center",
        )
        self.option3.pack(pady=5)

        self.nav_frame = tk.Frame(self, bg="#fbe8ea")
        self.nav_frame.pack(pady=20)

        # Bouton portrait robot
        self.portrait = tk.Button(
            self.nav_frame,
            text="Je crée mon portrait robot →",
            font=font_button,
            bg="#e1a4b6",
            fg="white",
            relief="flat",
            command=self.go_to_avatar_creation,
        )
        self.portrait.pack(side=tk.RIGHT, padx=100)

        # Bouton final
        self.jecree = tk.Button(
            self.nav_frame,
            text="← Je ne créé pas mon portrait robot",
            font=font_button,
            bg="#e1a4b6",
            fg="white",
            relief="flat",
            command=self.go_to_questions,
        )
        self.jecree.pack(side=tk.LEFT, padx=100)

    def open_avatar_creation(self):
        self.window_controller.go_to_window(
            self, AvatarCreationView(self.user_controller, self.window_controller, self.username)
        )

    def enregistrer_data(self):
        name = self.entry1.get()
        surname = self.entry2.get()
        age = self.age_value.get()
        genre = self.choix.get()

        user_information = UserPersonalInformation(name, surname, age, genre)
        self.user_controller.create_user(self.username, user_information)

        print("Données enregistrées pour :", self.username)

    def go_to_questions(self):
        if not self.entry1.get() or not self.entry2.get():
            tk.messagebox.showerror("Erreur", "Tous les champs doivent être remplis.")
            return

        self.enregistrer_data()
        self.window_controller.go_to_window(self, QuestionsView(self.user_controller, self.window_controller, self.username))

    def go_to_avatar_creation(self):
        if not self.entry1.get() or not self.entry2.get():
            tk.messagebox.showerror("Erreur", "Tous les champs doivent être remplis.")
            return

        self.enregistrer_data()
        self.open_avatar_creation()


if __name__ == "__main__":
    app = UserCreationView()
    app.mainloop()
