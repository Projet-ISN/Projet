# -*- coding: utf-8 -*-
"""
Created on Thu May 22 08:12:43 2025

@author: stani
"""

import tkinter as tk
from tkinter import ttk


class FenetreRobot:
    def __init__(self, root):
        self.root = root
        self.root.title("Portrait Robot")

        # Canvas pour dessin du robot
        self.canvas = tk.Canvas(root, width=400, height=400, bg='white') #fond blanc du canva dessiné
        self.canvas.grid(row=0, column=1, padx=10, pady=10, sticky='n') #placement du canva : sticky permet de laisser le canva en haut (n = north)

        # Notebook pour onglets de contrôle
        self.notebook = ttk.Notebook(root) #permet d'avoir plusieurs onglets
        self.notebook.grid(row=0, column=0, sticky='nsew', padx=10, pady=10) #nsew lui permet de prendre toute la place dans toutes les directions de la fenetre.

        # Création des frames pour chaque onglet
        self.frames = {}
        categories = ["Cheveux", "Oreilles", "Nez", "Yeux", "Bouche", "Couleurs"]
        for cat in categories: #créé un onglet pour chaque catégories
            frame = ttk.Frame(self.notebook, padding=10)  #padding = marge
            self.notebook.add(frame, text=cat)
            self.frames[cat.lower()] = frame

        # Variables tkinter par defaut
        self.style_vars = {
            "cheveux": tk.StringVar(value="Longs"),
            "oreilles": tk.StringVar(value="Ronde"),
            "nez": tk.StringVar(value="Petit"),
            "yeux_forme": tk.StringVar(value="Rond"),
            "bouche": tk.StringVar(value="Sourire"),
        }
        self.eye_color = tk.StringVar(value="bleu")
        self.hair_color = tk.StringVar(value="#FAEBA7")  # Teinte de blond très clair 
        self.skin_tone = tk.IntVar(value=30)

        self.create_controls()
        self.update_canvas()

        # Pour que la fenêtre s'adapte bien
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)

    def create_controls(self):
        # Cheveux
        frame = self.frames["cheveux"]
        ttk.Label(frame, text="Style des cheveux :").pack(anchor="w")
        for option in ["Longs", "Courts"]:
            ttk.Radiobutton(frame, text=option, variable=self.style_vars["cheveux"], value=option, command=self.update_canvas).pack(anchor='w')

        ttk.Label(frame, text="Couleur des cheveux :").pack(anchor="w", pady=(10,0))
        color_options = {
            "Blond très clair": "#FAEBA7",
            "Blond foncé": "#D4B157",
            "Roux": "#F47011",
            "Châtain": "#7B4E20",
            "Brun": "#29130A"
        }
        for label, hexcode in color_options.items():
            ttk.Radiobutton(frame, text=label, variable=self.hair_color, value=hexcode, command=self.update_canvas).pack(anchor='w')

        # Oreilles
        frame = self.frames["oreilles"]
        ttk.Label(frame, text="Forme des oreilles :").pack(anchor="w")
        for option in ["Ronde", "Carrée", "Antenne"]:
            ttk.Radiobutton(frame, text=option, variable=self.style_vars["oreilles"], value=option, command=self.update_canvas).pack(anchor='w')

        # Nez
        frame = self.frames["nez"]
        ttk.Label(frame, text="Forme du nez :").pack(anchor="w")
        for option in ["Petit", "Grand", "Pointu"]:
            ttk.Radiobutton(frame, text=option, variable=self.style_vars["nez"], value=option, command=self.update_canvas).pack(anchor='w')

        # Yeux
        frame = self.frames["yeux"]
        ttk.Label(frame, text="Forme des yeux :").pack(anchor="w")
        for option in ["Rond", "Carré", "Triangle"]:
            ttk.Radiobutton(frame, text=option, variable=self.style_vars["yeux_forme"], value=option, command=self.update_canvas).pack(anchor='w')

        ttk.Label(frame, text="Couleur des yeux :").pack(anchor="w", pady=(10,0))
        for color in ["bleu", "vert", "marron", "noir"]:
            ttk.Radiobutton(frame, text=color.capitalize(), variable=self.eye_color, value=color, command=self.update_canvas).pack(anchor='w')

        # Bouche
        frame = self.frames["bouche"]
        ttk.Label(frame, text="Forme de la bouche :").pack(anchor="w")
        for option in ["Sourire", "Droite", "Triste"]:
            ttk.Radiobutton(frame, text=option, variable=self.style_vars["bouche"], value=option, command=self.update_canvas).pack(anchor='w')

        # Couleurs (peau)
        frame = self.frames["couleurs"]
        ttk.Label(frame, text="Couleur de la peau :").pack(anchor="w")
        skin_scale = tk.Scale(frame, from_=0, to=100, orient='horizontal', variable=self.skin_tone,
                              label="Clair → Foncé", command=lambda e: self.update_canvas())
        skin_scale.pack(fill='x', pady=10)

        # Bouton Mettre à jour (optionnel)
        btn = ttk.Button(frame, text="Mettre à jour les changements", command=self.update_canvas)
        btn.pack(pady=10)

    def get_skin_color(self):  #commande permettantd'ajuster la couleur de peau, trouvée sur internet
        t = self.skin_tone.get() / 100
        r = int((1 - t) * 245 + t * 85)
        g = int((1 - t) * 222 + t * 60)
        b = int((1 - t) * 179 + t * 40)
        return f'#{r:02x}{g:02x}{b:02x}'

    def update_canvas(self):
        self.canvas.delete("all")

        skin_color = self.get_skin_color()
        hair_color = self.hair_color.get()

        # Tête
        self.canvas.create_oval(100, 100, 300, 300, fill=skin_color, outline="black")

        # Cheveux
        style_cheveux = self.style_vars["cheveux"].get()
        if style_cheveux == "Longs":
            self.canvas.create_rectangle(100, 60, 300, 120, fill=hair_color)
        elif style_cheveux == "Courts":
            self.canvas.create_rectangle(150, 80, 250, 110, fill=hair_color)

        # Oreilles (forme + couleur noire fixe)
        style_oreilles = self.style_vars["oreilles"].get()
        if style_oreilles == "Ronde":
            self.canvas.create_oval(70, 150, 90, 190, fill="black")
            self.canvas.create_oval(310, 150, 330, 190, fill="black")
        elif style_oreilles == "Carrée":
            self.canvas.create_rectangle(70, 150, 90, 190, fill="black")
            self.canvas.create_rectangle(310, 150, 330, 190, fill="black")
        elif style_oreilles == "Antenne":
            self.canvas.create_line(80, 150, 80, 100, fill="black", width=3)
            self.canvas.create_line(320, 150, 320, 100, fill="black", width=3)

        # Yeux (forme + couleur)
        form_yeux = self.style_vars["yeux_forme"].get()
        color_map = {
            "bleu": "#0000ff",
            "vert": "#00cc00",
            "marron": "#804000",
            "noir": "#000000"
        }
        eye_color = color_map[self.eye_color.get()]
        if form_yeux == "Rond":
            self.canvas.create_oval(150, 150, 170, 170, fill=eye_color)
            self.canvas.create_oval(230, 150, 250, 170, fill=eye_color)
        elif form_yeux == "Carré":
            self.canvas.create_rectangle(150, 150, 170, 170, fill=eye_color)
            self.canvas.create_rectangle(230, 150, 250, 170, fill=eye_color)
        elif form_yeux == "Triangle":
            self.canvas.create_polygon(160, 150, 150, 170, 170, 170, fill=eye_color)
            self.canvas.create_polygon(240, 150, 230, 170, 250, 170, fill=eye_color)

        # Nez (forme uniquement)
        style_nez = self.style_vars["nez"].get()
        if style_nez == "Petit":
            self.canvas.create_oval(190, 180, 210, 200, fill="black")
        elif style_nez == "Grand":
            self.canvas.create_oval(180, 170, 220, 210, fill="black")
        elif style_nez == "Pointu":
            self.canvas.create_polygon(200, 170, 190, 210, 210, 210, fill="black")

        # Bouche
        style_bouche = self.style_vars["bouche"].get()
        if style_bouche == "Sourire":
            self.canvas.create_arc(160, 220, 240, 260, start=0, extent=-180, style=tk.ARC, outline="black", width=3)
        elif style_bouche == "Droite":
            self.canvas.create_line(160, 240, 240, 240, fill="black", width=3)
        elif style_bouche == "Triste":
            self.canvas.create_arc(160, 240, 240, 280, start=0, extent=180, style=tk.ARC, outline="black", width=3)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("900x500")
    app = FenetreRobot(root)
    root.mainloop()
