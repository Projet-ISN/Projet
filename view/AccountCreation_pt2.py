# -*- coding: utf-8 -*-
"""
Created on Mon May 26 10:20:12 2025

@author: stani
"""

import tkinter as tk
from tkinter import *
from view.Portrait_robot_v2 import FenetreRobot
import json
import os

class CreationCompte(tk.Tk) : 
    
    def __init__(self, user_controller, window_controller, username) :
        super().__init__()
        
        self.geometry("750x400")
        self.title("Création de ton compte ...")
        self.user_controller = user_controller
        self.window_controller = window_controller
        self.username = username
        
        
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
        
        self.age_value = tk.IntVar(value=18)
        self.Scale = tk.Scale(self, from_= 18, to = 99, variable = self.age_value, orient = tk.HORIZONTAL)
        self.Scale.pack(side = tk.TOP) 
        
        self.text2 = tk.Label(self, text = 'Genre :')
        self.text2.pack(side = tk.TOP) 
       
        
        self.choix = tk.StringVar(value="Non renseigné")
        
        self.option1 = tk.Radiobutton(self, text = 'Homme', variable = self.choix, value = "Homme")
        self.option1.pack(side = tk.TOP) 
        self.option2 = tk.Radiobutton(self, text = 'Femme', variable = self.choix, value = "Femme")
        self.option2.pack(side = tk.TOP) 
        self.option3 = tk.Radiobutton(self, text = 'Autre', variable = self.choix, value = "Autre")
        self.option3.pack(side = tk.TOP) 
        
        #definir son portrait robot
        self.portrait = tk.Button(self, text = 'Je crée mon portrait robot')
        self.portrait.pack(side=tk.TOP, pady = 30)
        self.portrait.bind('<Button-1>',self.open_avatar_creation)
        
        #bouton
        self.jecree = tk.Button(self, text = 'Je crée mon compte')
        self.jecree.pack(side=tk.RIGHT, padx = 60)
        self.jecree.bind('<Button-1>',self.enregistrer_data)

        self.bind("<Escape>", lambda e: self.attributes("-fullscreen", False))

    def open_avatar_creation(self,event) :
        root = tk.Tk()
        self.window_controller.go_to_window(self,FenetreRobot(root))
        
    def enregistrer_data(self,event):
        user_data = {  
            "username" : self.username,
            "prenom" : self.entry1.get(),
            "nom" : self.entry2.get(),
            "age" : self.age_value.get(),
            "genre" : self.choix.get()}
        dossier = "users/" #A modifier en fonction du chemin du dossier
        os.makedirs(dossier, exist_ok=True)

        chemin_fichier = os.path.join(dossier, self.username+".json")  
        
        with open(chemin_fichier, "w") as fichier:
            json.dump(user_data, fichier, indent=4)
        
        print("Data enregistrée")
        