# -*- coding: utf-8 -*-
"""
Created on Mon May 26 10:20:12 2025

@author: stani
"""

import tkinter as tk
from tkinter import *

class CreationCompte(tk.Tk) : 
    
    def __init__(self) :
        super().__init__()
        
        self.geometry("750x400")
        self.title("Création de ton compte ...")
        
        
        self.prenom = tk.Label(self, text = 'Prénom :')
        self.prenom.pack(side = tk.TOP) 
        
        self.entry1 = tk.Entry(self)
        self.entry1.pack(side = tk.TOP) 
        
        self.nom = tk.Label(self, text = 'Nom :')
        self.nom.pack(side = tk.TOP) 
        
        self.entry2 = tk.Entry(self)
        self.entry2.pack(side = tk.TOP) 
        
        
        self.text1 = tk.Label(self, text = 'Âge :')
        self.text1.pack(side = tk.TOP) 
        
        self.Scale = tk.Scale(self, from_= 18, to = 99, orient = tk.HORIZONTAL)
        self.Scale.pack(side = tk.TOP) 
        
        self.text2 = tk.Label(self, text = 'Genre :')
        self.text2.pack(side = tk.TOP) 
       
        
        self.choix = tk.IntVar()
        self.choix.set(0)
        
        self.option1 = tk.Radiobutton(self, text = 'Homme', variable = self.choix, value = 1)
        self.option1.pack(side = tk.TOP) 
        self.option2 = tk.Radiobutton(self, text = 'Femme', variable = self.choix, value = 2)
        self.option2.pack(side = tk.TOP) 
        self.option3 = tk.Radiobutton(self, text = 'Autre', variable = self.choix, value = 3)
        self.option3.pack(side = tk.TOP) 
        
        #definir son portrait robot
        self.portrait = tk.Button(self, text = 'Je crée mon portrait robot')
        self.portrait.pack(side=tk.TOP, pady = 30)
        
        #bouton
        self.jecree = tk.Button(self, text = 'Je crée mon compte')
        self.jecree.pack(side=tk.RIGHT, padx = 60)

        self.bind("<Escape>", lambda e: self.attributes("-fullscreen", False))

    #def CreerCompte() :
        
        
        
        
    
app = CreationCompte()
app.mainloop()
