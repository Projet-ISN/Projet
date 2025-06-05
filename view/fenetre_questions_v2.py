# -*- coding: utf-8 -*-
"""
Created on Wed Jun  4 20:04:26 2025

@author: stani
"""
import tkinter as tk
from tkinter import *

class VueQuestions(tk.Tk): 
    def __init__(self, question): 
        super().__init__()

        self.question = question
        self.title("Pour en apprendre plus sur vous")
        self.attributes('-fullscreen', True) #ouverture en plein écran par défaut
        self.configure(bg="#fbe8ea") #couleur de fond
        
        #affichage de la question
        self.text = tk.Label(self, text=question['question'], font=("Helvetica", 22, "bold"), wraplength=1000, justify="center", bg="#fbe8ea", fg="#4b2e2e")
        self.text.pack(pady=70)

        self.middle = tk.Frame(self, bg="#fbe8ea")
        self.middle.pack(pady=30)
        
        #la personne peut entrer une valeur sur une échelle de 1 à 10 pour dire à quel point cette question est importante selon elle
        self.importance = tk.Label(self.middle, text="Importance de cette question selon vous :", font=("Helvetica", 20), bg="#fbe8ea", fg="#4b2e2e")
        self.importance.pack(pady=20)
        
        self.sc1 = tk.Scale(
            self.middle,
            from_=1,
            to=10,
            orient='horizontal',
            length=800,
            sliderlength=40,
            width=25,
            font=("Helvetica", 16),
            bg="#fbe8ea",
            fg="#4b2e2e",
            troughcolor="#e1a4b6",
            highlightbackground="#fbe8ea",
            activebackground="#fbe8ea",
        )
        self.sc1.pack(pady=15)

        self.frame = tk.Frame(self, bg="#fbe8ea")
        self.frame.pack()
        #si la question est à choix multiple
        if self.question['choix'] == 'multiple': 
            self.choix1 = tk.BooleanVar()
            self.choix2 = tk.BooleanVar()
            self.choix3 = tk.BooleanVar()
            self.choix4 = tk.BooleanVar()

            self.cb1 = tk.Checkbutton(self.frame, text=self.question['options'][0], variable=self.choix1, bg="#fbe8ea", fg="#4b2e2e", font=("Helvetica", 18), activebackground="#fbe8ea", selectcolor="#ffe6ec")
            self.cb1.pack(pady=10)
            self.cb2 = tk.Checkbutton(self.frame, text=self.question['options'][1], variable=self.choix2, bg="#fbe8ea", fg="#4b2e2e", font=("Helvetica", 18), activebackground="#fbe8ea", selectcolor="#ffe6ec")
            self.cb2.pack(pady=10)
            self.cb3 = tk.Checkbutton(self.frame, text=self.question['options'][2], variable=self.choix3, bg="#fbe8ea", fg="#4b2e2e", font=("Helvetica", 18), activebackground="#fbe8ea", selectcolor="#ffe6ec")
            self.cb3.pack(pady=10)
            self.cb4 = tk.Checkbutton(self.frame, text=self.question['options'][3], variable=self.choix4, bg="#fbe8ea", fg="#4b2e2e", font=("Helvetica", 18), activebackground="#fbe8ea", selectcolor="#ffe6ec")
            self.cb4.pack(pady=50)
        
        #sinon si elle est à choix unique
        elif self.question['choix'] == 'unique': 
            self.choix = tk.IntVar()
            self.choix.set(0)

            self.rb1 = tk.Radiobutton(self.frame, text=self.question['options'][0], variable=self.choix, value=1, bg="#fbe8ea", fg="#4b2e2e", font=("Helvetica", 18), activebackground="#fbe8ea", selectcolor="#ffe6ec")
            self.rb1.pack(pady=10)
            self.rb2 = tk.Radiobutton(self.frame, text=self.question['options'][1], variable=self.choix, value=2, bg="#fbe8ea", fg="#4b2e2e", font=("Helvetica", 18), activebackground="#fbe8ea", selectcolor="#ffe6ec")
            self.rb2.pack(pady=10)
            self.rb3 = tk.Radiobutton(self.frame, text=self.question['options'][2], variable=self.choix, value=3, bg="#fbe8ea", fg="#4b2e2e", font=("Helvetica", 18), activebackground="#fbe8ea", selectcolor="#ffe6ec")
            self.rb3.pack(pady=10)
            self.rb4 = tk.Radiobutton(self.frame, text=self.question['options'][3], variable=self.choix, value=4, bg="#fbe8ea", fg="#4b2e2e", font=("Helvetica", 18), activebackground="#fbe8ea", selectcolor="#ffe6ec")
            self.rb4.pack(pady=10)

        self.nav_frame = tk.Frame(self, bg="#fbe8ea")
        self.nav_frame.pack(pady=120)
        
        #boutons précédent et suivant
        self.prec = tk.Button(self.nav_frame, text='← Précédent', font=("Helvetica", 14), bg="#e1a4b6", fg="white", relief="flat", padx=30, pady=10)
        self.prec.pack(side="left", padx=100, pady=70)

        self.suiv = tk.Button(self.nav_frame, text='Suivant →', font=("Helvetica", 14), bg="#e1a4b6", fg="white", relief="flat", padx=30, pady=10)
        self.suiv.pack(side="right", padx=100, pady=70)

        self.bind("<Escape>", lambda e: self.attributes("-fullscreen", False))


if __name__ == "__main__":
    # Exemple d’appel
    question = {
        'question': 'Quel type de personne recherchez-vous ?',
        'choix': 'unique',
        'options': ['Ambitieuse', 'Aventurière', 'Romantique', 'Calme']
    }
    
    app = VueQuestions(question)
    app.mainloop()
