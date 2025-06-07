import tkinter as tk

from model.User import User
from model.UserAccountInformation import UserAccountInformation
from view.AccountCreation_pt2 import CreationCompte

class AccountCreationView(tk.Tk):
    def __init__(self, user_controller, window_controller):
        super().__init__()
        self.geometry("450x300")
        self.title("Création de compte")
        
        self.user_controller = user_controller
        self.window_controller = window_controller

        # Nom d'utilisateur
        self.username_label = tk.Label(self, text="Nom d'utilisateur :")
        self.username_label.pack(side=tk.TOP)
        self.username_entry = tk.Entry(self)
        self.username_entry.pack(side=tk.TOP)

        # Mot de passe
        self.password_label = tk.Label(self, text="Mot de passe :")
        self.password_label.pack(side=tk.TOP)
        self.password_entry = tk.Entry(self, show='*')
        self.password_entry.pack(side=tk.TOP)

        self.password_confirm_label = tk.Label(self, text="Confirmer le mot de passe :")
        self.password_confirm_label.pack(side=tk.TOP)
        self.password_confirm_entry = tk.Entry(self, show='*')
        self.password_confirm_entry.pack(side=tk.TOP, pady = 10)

        # Bouton de création de compte
        self.create_account_button = tk.Button(self, text="Créer un compte", command=self.manage_button_click)
        self.create_account_button.pack(side=tk.TOP, pady = 50)

    
    def manage_button_click(self):
        self.create_account()
        self.open_avatar_creation()
    
    
    def create_account(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        password_confirm = self.password_confirm_entry.get()

        if password != password_confirm:
            tk.messagebox.showerror("Erreur", "Les mots de passe ne correspondent pas.")
            return
        

        user_information = UserAccountInformation(username, password)
        user = User(user_information)

        self.user_controller.create_user(user)
        print(f"Compte créé pour l'utilisateur : {username}")
        
    def open_avatar_creation(self):
        self.window_controller.go_to_window(self, CreationCompte(self.user_controller, self.window_controller))