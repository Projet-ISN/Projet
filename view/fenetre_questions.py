# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tkinter as tk
from tkinter import *

class VueQuestions(tk.Tk) : 
    
    def __init__(self, question) : #question est un dico avec { 'question' : XXX, 'choix' : 'unique'/ 'multiple', 'options':[option1, option2, option3, option4] }
        super().__init__()
        self.question = question
        
        self.geometry("750x400")
        self.title("Pour en apprendre plus sur vous")
        
        self.text = tk.Label(self, text = question['question'])
        self.text.pack(side=tk.TOP) #la question est en haut de la fenêtre
        
        #à quel point la question est importante pour l'utilisateur
        self.importance = tk.Label(self, text = "Importance de cette question selon vous :")
        self.importance.pack(side=tk.TOP)
        self.sc1 = tk.Scale(self, from_ = 1, to = 10, orient = 'horizontal')
        self.sc1.pack(side=tk.TOP)
        
        #options de réponses
        self.frame = tk.Frame(self)
        self.frame.pack(side=tk.TOP)
        
        if self.question['choix'] == 'multiple' : 
            self.choix1 = tk.BooleanVar()  #défini sur False par defaut
            self.choix2 = tk.BooleanVar()
            self.choix3 = tk.BooleanVar()
            self.choix4 = tk.BooleanVar()
            self.option1 = tk.Checkbutton(self.frame, text = self.question['options'][0], variable = self.choix1, onvalue = True)
            self.option1.grid(row=1, column=0)
            self.option2 = tk.Checkbutton(self.frame, text = self.question['options'][1], variable = self.choix2, onvalue = True)
            self.option2.grid(row=2, column=0)
            self.option3 = tk.Checkbutton(self.frame, text = self.question['options'][2], variable = self.choix3, onvalue = True)
            self.option3.grid(row=3, column=0)
            self.option4 = tk.Checkbutton(self.frame, text = self.question['options'][3], variable = self.choix4, onvalue = True)
            self.option4.grid(row=4, column=0)
            
        if question['choix'] == 'unique' : 
            self.choix = tk.IntVar()
            self.choix.set(0)
            self.option1 = tk.Radiobutton(self.frame, text = self.question['options'][0], variable = self.choix, value = 1)
            self.option1.grid(row=1, column=0)
            self.option2 = tk.Radiobutton(self.frame, text = self.question['options'][1], variable = self.choix, value = 2)
            self.option2.grid(row=2, column=0)
            self.option3 = tk.Radiobutton(self.frame, text = self.question['options'][2], variable = self.choix, value = 3)
            self.option3.grid(row=3, column=0)
            self.option4 = tk.Radiobutton(self.frame, text = self.question['options'][3], variable = self.choix, value = 4)
            self.option4.grid(row=4, column=0)
        
        
        #boutons suivant et précédent
        self.suiv = tk.Button(self, text = 'suivant')
        self.suiv.pack(side=tk.RIGHT, padx = 60)
        self.prec = tk.Button(self, text = 'précédent')
        self.prec.pack(side=tk.LEFT, padx = 60)
        
        

question = { 'question' : 'XXX', 'choix' : 'multiple', 'options':['option1', 'option2', 'option3', 'option4'] }


app = VueQuestions(question)
app.mainloop()




















