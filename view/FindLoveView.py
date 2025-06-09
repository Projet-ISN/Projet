#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  9 11:16:16 2025

@author: mtobonguev
"""

import tkinter as tk
from controller.AccountController import AccountController
from controller.UserController import UserController
from controller.WindowController import WindowController


class FindLoveView(tk.Toplevel):
    def __init__(self,username):
        super().__init__()
        self.title("Résultats de l'appariement")
        self.configure(bg="#fbe8ea")
        self.attributes("-fullscreen", True)
        self.bind("<Escape>", lambda e: self.attributes("-fullscreen", False))
        
        self.username = username
        
        font_button = ("Helvetica", 16)
        
        # Frame principale
        main_frame = tk.Frame(self, bg="#fbe8ea")
        main_frame.pack(expand=True, pady=10)

        tk.Label(
            main_frame,
            text="Bienvenue "+self.username,
            font=("Helvetica", 24, "bold"),
            bg="#fbe8ea",
        ).pack(pady=40)
        
        self.find_love_button = tk.Button(
            main_frame,
            text="Trouver ton amour <3",
            font=font_button,
            bg="#e1a4b6",
            fg="white",
            relief="flat",
            #command=self.open_questions_importance_vue
            )
        self.find_love_button.pack(pady=60)
        
    # def open_questions_importance_vue(self):
        # self.WindowController.go_to_window(self,QuestionsImportanceView())
        
if __name__ == "__main__":
     user = "mtobon"
     app = FindLoveView(user)
     app.mainloop()
        
