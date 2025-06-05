# -*- coding: utf-8 -*-
"""
Created on Thu Jun  5 08:34:12 2025

@author: stani
"""

import tkinter as tk
from tkinter import *

class CreationCompte(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Création de ton compte")
        self.geometry("800x600")
        self.configure(bg="#fbe8ea")
        self.attributes('-fullscreen', True)
        self.bind("<Escape>", lambda e: self.attributes("-fullscreen", False))

        # Style général
        font_label = ("Helvetica", 20)
        font_entry = ("Helvetica", 20)
        font_button = ("Helvetica", 16)
        
        self.frame_gen = tk.Frame(self, bg="#fbe8ea")
        self.frame_gen.pack(pady = 40)
        
        self.prenom = tk.Label(self.frame_gen, text="Donne nous tes petites informations !", font=("Helvetica", 24, "bold"), bg="#fbe8ea")
        self.prenom.pack(pady=80)
        # Prénom
        self.prenom = tk.Label(self.frame_gen, text="Prénom :", font=font_label, bg="#fbe8ea")
        self.prenom.pack(pady=5)
        self.entry1 = tk.Entry(self.frame_gen, font=font_entry, justify='center')
        self.entry1.pack(pady=20)

        # Nom
        self.nom = tk.Label(self.frame_gen, text="Nom :", font=font_label, bg="#fbe8ea")
        self.nom.pack(pady=5)
        self.entry2 = tk.Entry(self.frame_gen, font=font_entry, justify='center')
        self.entry2.pack(pady=20)

        # Âge
        self.text1 = tk.Label(self.frame_gen, text="Âge :", font=font_label, bg="#fbe8ea")
        self.text1.pack(pady=10)
        self.scale = tk.Scale(self.frame_gen, from_=18, to=99, orient=tk.HORIZONTAL, font=("Helvetica", 16),
                              bg="#fbe8ea", length=400)
        self.scale.pack(pady=20)
        
        # Genre
        self.text2 = tk.Label(self.frame_gen, text="Genre :", font=font_label, bg="#fbe8ea")
        self.text2.pack(pady=10)

        self.choix = tk.IntVar()
        self.choix.set(0)
        self.option1 = tk.Radiobutton(self.frame_gen, text="Homme", variable=self.choix, value=1,
                                      font=font_label, bg="#fbe8ea", anchor="w", justify="center")
        self.option1.pack(pady=5)
        self.option2 = tk.Radiobutton(self.frame_gen, text="Femme", variable=self.choix, value=2,
                                      font=font_label, bg="#fbe8ea", anchor="w", justify="center")
        self.option2.pack(pady=5)
        self.option3 = tk.Radiobutton(self.frame_gen, text="Autre", variable=self.choix, value=3,
                                      font=font_label, bg="#fbe8ea", anchor="w", justify="center")
        self.option3.pack(pady=5)
        
        self.nav_frame = tk.Frame(self, bg="#fbe8ea")
        self.nav_frame.pack() 
        
        # Bouton portrait robot
        self.portrait = tk.Button(self.nav_frame, text="Je crée mon portrait robot →", font=font_button, bg="#e1a4b6", fg="white", relief="flat")
        self.portrait.pack(side="right", padx=100, pady=70)

        # Bouton final
        self.jecree = tk.Button(self.nav_frame, text="← Je ne créé pas mon portrait robot", font=font_button, bg="#e1a4b6", fg="white", relief="flat")
        self.jecree.pack(side="right", padx=100, pady=70)

if __name__ == "__main__":
    app = CreationCompte()
    app.mainloop()
