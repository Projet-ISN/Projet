import tkinter as tk
from controller.UserController import UserController
from controller.WindowController import WindowController
from model.UserPersonalInformation import UserPersonalInformation
from view.AvatarCreationView import AvatarCreationView
from view.QuestionsView import QuestionsView
from tkinter import messagebox


class UserCreationView(tk.Toplevel):
    def __init__(
        self,
        user_controller: UserController,
        window_controller: WindowController,
        username,
    ):
        super().__init__()

        self.title("Création de ton compte")
        self.configure(bg="#fbe8ea")
        self.attributes("-fullscreen", True)
        self.bind("<Escape>", lambda e: self.attributes("-fullscreen", False))

        self.user_controller = user_controller
        self.window_controller = window_controller
        self.username = username

        screen_height = self.winfo_screenheight()

        font_title = ("Helvetica", int(screen_height * 0.035), "bold")
        font_label = ("Helvetica", int(screen_height * 0.027))
        font_entry = ("Helvetica", int(screen_height * 0.027))
        font_button = ("Helvetica", int(screen_height * 0.023))
        font_scale = ("Helvetica", int(screen_height * 0.022))

        pady_section = int(screen_height * 0.015)
        pady_entry = int(screen_height * 0.02)
        padx_button = int(screen_height * 0.07)

        self.frame_gen = tk.Frame(self, bg="#fbe8ea")
        self.frame_gen.pack(pady=pady_section)

        tk.Label(
            self.frame_gen,
            text="Donne nous tes petites informations !",
            font=font_title,
            bg="#fbe8ea",
        ).pack(pady=pady_section * 2)

        # Prénom
        tk.Label(self.frame_gen, text="Prénom :", font=font_label, bg="#fbe8ea").pack(
            pady=5
        )
        self.entry1 = tk.Entry(self.frame_gen, font=font_entry, justify="center")
        self.entry1.pack(pady=pady_entry)

        # Nom
        tk.Label(self.frame_gen, text="Nom :", font=font_label, bg="#fbe8ea").pack(
            pady=5
        )
        self.entry2 = tk.Entry(self.frame_gen, font=font_entry, justify="center")
        self.entry2.pack(pady=pady_entry // 2)

        # Âge
        self.age_value = tk.IntVar(value=18)
        tk.Label(self.frame_gen, text="Âge :", font=font_label, bg="#fbe8ea").pack(
            pady=pady_section
        )
        self.scale = tk.Scale(
            self.frame_gen,
            from_=18,
            to=99,
            variable=self.age_value,
            orient=tk.HORIZONTAL,
            font=font_scale,
            bg="#fbe8ea",
            length=400,
        )
        self.scale.pack(pady=pady_entry)

        # Genre
        tk.Label(self.frame_gen, text="Genre :", font=font_label, bg="#fbe8ea").pack(
            pady=pady_section
        )

        self.choix = tk.StringVar(value="Non renseigné")
        for genre in ["Homme", "Femme", "Autre"]:
            tk.Radiobutton(
                self.frame_gen,
                text=genre,
                variable=self.choix,
                value=genre,
                font=font_label,
                bg="#fbe8ea",
                anchor="w",
                justify="center",
            ).pack(pady=5)

        self.nav_frame = tk.Frame(self, bg="#fbe8ea")
        self.nav_frame.pack(pady=pady_section)

        # Bouton portrait robot
        tk.Button(
            self.nav_frame,
            text="Je crée mon portrait robot →",
            font=font_button,
            bg="#e1a4b6",
            fg="white",
            relief="flat",
            command=self.go_to_avatar_creation,
        ).pack(side=tk.RIGHT, padx=padx_button)

        # Bouton final
        tk.Button(
            self.nav_frame,
            text="← Je ne créé pas mon portrait robot",
            font=font_button,
            bg="#e1a4b6",
            fg="white",
            relief="flat",
            command=self.go_to_questions,
        ).pack(side=tk.LEFT, padx=padx_button)

    def open_avatar_creation(self):
        self.window_controller.go_to_window(
            self,
            AvatarCreationView(
                self.user_controller, self.window_controller, self.username
            ),
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
            messagebox.showerror("Erreur", "Tous les champs doivent être remplis.")
            return

        self.enregistrer_data()
        self.window_controller.go_to_window(
            self,
            QuestionsView(self.user_controller, self.window_controller, self.username),
        )

    def go_to_avatar_creation(self):
        if not self.entry1.get() or not self.entry2.get():
            messagebox.showerror("Erreur", "Tous les champs doivent être remplis.")
            return

        self.enregistrer_data()
        self.open_avatar_creation()
