#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  9 12:53:53 2025

@author: mtobonguev
"""

import tkinter as tk


class ResultsView(tk.Toplevel):
    def __init__(self, results):
        super().__init__()
        self.title("Résultats de l'appariement")
        self.attributes("-fullscreen", True)  # ouverture en plein écran par défaut
        self.configure(bg="#fbe8ea")  # couleur de fond
        self.bind("<Escape>", lambda e: self.attributes("-fullscreen", False))

        self.results = results

        # Style général
        font_label = ("Helvetica", 20)

        # Frame principale
        main_frame = tk.Frame(self, bg="#fbe8ea")
        main_frame.pack(expand=True, pady=10)

        tk.Label(
            main_frame,
            text="Ton match idéal est...",
            font=("Helvetica", 24, "bold"),
            bg="#fbe8ea",
        ).pack(pady=20)

        self.match1 = tk.Label(
            main_frame,
            text=self.results[0]["username"]
            + " avec "
            + str(self.results[0]["compatibility"])
            + "% de compatibilité",
            font=font_label,
            bg="#fbe8ea",
        )
        self.match1.pack(pady=10)

        self.autres_matchs = tk.Label(
            main_frame,
            text="Autres matchs possibles :",
            font=("Helvetica", 20, "bold"),
            bg="#fbe8ea",
        )
        self.autres_matchs.pack(pady=(25))

        self.match2 = tk.Label(
            main_frame,
            text=self.results[1]["username"]
            + " avec "
            + str(self.results[1]["compatibility"])
            + "% de compatibilité",
            font=font_label,
            bg="#fbe8ea",
        )
        self.match2.pack(pady=(5))

        self.match3 = tk.Label(
            main_frame,
            text=self.results[2]["username"]
            + " avec "
            + str(self.results[2]["compatibility"])
            + "% de compatibilité",
            font=font_label,
            bg="#fbe8ea",
        )
        self.match3.pack(pady=(5))
