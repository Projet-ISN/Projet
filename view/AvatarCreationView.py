import tkinter as tk
from tkinter import ttk


class AvatarCreationView(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Portrait Robot")
        self.attributes("-fullscreen", True)
        self.configure(bg="#fbe8ea")
        self.bind("<Escape>", lambda e: self.attributes("-fullscreen", False))

        # Style
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TNotebook", background="#fbe8ea", borderwidth=0)
        style.configure(
            "TNotebook.Tab",
            background="#e1a4b6",
            foreground="white",
            font=("Helvetica", 20),
            padding=10,
        )
        style.configure("TFrame", background="#fbe8ea")
        style.configure(
            "TLabel", background="#fbe8ea", font=("Helvetica", 20), foreground="#4b2e2e"
        )
        style.configure(
            "TRadiobutton",
            background="#fbe8ea",
            font=("Helvetica", 20),
            foreground="#4b2e2e",
        )
        style.configure(
            "TButton", background="#e1a4b6", foreground="white", font=("Helvetica", 20)
        )

        # Canvas
        self.canvas = tk.Canvas(
            self, width=1000, height=1000, bg="#fbe8ea", highlightthickness=0
        )
        self.canvas.grid(row=0, column=1, padx=40, pady=40, sticky="n")

        # Notebook avec différents onglets
        self.notebook = ttk.Notebook(self)
        self.notebook.grid(row=0, column=0, sticky="nsew", padx=40, pady=40)

        self.frames = {}
        categories = ["Cheveux", "Oreilles", "Nez", "Yeux", "Bouche", "Couleurs"]
        for cat in categories:
            frame = ttk.Frame(self.notebook, padding=20)
            self.notebook.add(frame, text=cat)
            self.frames[cat.lower()] = frame

        self.style_vars = {
            "cheveux": tk.StringVar(value="Longs"),
            "oreilles": tk.StringVar(value="Ronde"),
            "nez": tk.StringVar(value="Petit"),
            "yeux_forme": tk.StringVar(value="Rond"),
            "bouche": tk.StringVar(value="Sourire"),
        }
        self.eye_color = tk.StringVar(value="bleu")
        self.hair_color = tk.StringVar(value="#FAEBA7")
        self.skin_tone = tk.IntVar(value=30)

        self.creation_portrait()
        self.update_canvas()

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def update_canvas(self):
        """
        fonction qui met à jour le canva selon quel bouton est cliqué (quelles caractériqtiques)
        une partie de cette fonction a été générée par IA

        Returns
        -------
        None.

        """

        self.canvas.delete("all")

        skin_color = self.couleur_peau()
        hair_color = self.hair_color.get()

        center_x, center_y = 500, 500

        # Tête
        self.canvas.create_oval(
            center_x - 200,
            center_y - 200,
            center_x + 200,
            center_y + 200,
            fill=skin_color,
            outline="black",
        )

        # Cheveux
        style_cheveux = self.style_vars["cheveux"].get()
        if style_cheveux == "Longs":
            self.canvas.create_rectangle(
                center_x - 200,
                center_y - 240,
                center_x + 200,
                center_y - 180,
                fill=hair_color,
            )
        elif style_cheveux == "Courts":
            self.canvas.create_rectangle(
                center_x - 100,
                center_y - 200,
                center_x + 100,
                center_y - 170,
                fill=hair_color,
            )

        # Oreilles
        style_oreilles = self.style_vars["oreilles"].get()
        if style_oreilles == "Ronde":
            self.canvas.create_oval(
                center_x - 240,
                center_y - 50,
                center_x - 200,
                center_y + 50,
                fill="black",
            )
            self.canvas.create_oval(
                center_x + 200,
                center_y - 50,
                center_x + 240,
                center_y + 50,
                fill="black",
            )
        elif style_oreilles == "Carrée":
            self.canvas.create_rectangle(
                center_x - 240,
                center_y - 50,
                center_x - 200,
                center_y + 50,
                fill="black",
            )
            self.canvas.create_rectangle(
                center_x + 200,
                center_y - 50,
                center_x + 240,
                center_y + 50,
                fill="black",
            )
        elif style_oreilles == "Antenne":
            self.canvas.create_line(
                center_x - 230,
                center_y - 50,
                center_x - 230,
                center_y - 120,
                fill="black",
                width=6,
            )
            self.canvas.create_line(
                center_x + 230,
                center_y - 50,
                center_x + 230,
                center_y - 120,
                fill="black",
                width=6,
            )

        # Yeux
        form_yeux = self.style_vars["yeux_forme"].get()
        color_map = {
            "bleu": "#0000ff",
            "vert": "#00cc00",
            "marron": "#804000",
            "noir": "#000000",
        }
        eye_color = color_map[self.eye_color.get()]
        if form_yeux == "Rond":
            self.canvas.create_oval(
                center_x - 100,
                center_y - 50,
                center_x - 60,
                center_y - 10,
                fill=eye_color,
            )
            self.canvas.create_oval(
                center_x + 60,
                center_y - 50,
                center_x + 100,
                center_y - 10,
                fill=eye_color,
            )
        elif form_yeux == "Carré":
            self.canvas.create_rectangle(
                center_x - 100,
                center_y - 50,
                center_x - 60,
                center_y - 10,
                fill=eye_color,
            )
            self.canvas.create_rectangle(
                center_x + 60,
                center_y - 50,
                center_x + 100,
                center_y - 10,
                fill=eye_color,
            )
        elif form_yeux == "Triangle":
            self.canvas.create_polygon(
                center_x - 80,
                center_y - 50,
                center_x - 100,
                center_y - 10,
                center_x - 60,
                center_y - 10,
                fill=eye_color,
            )
            self.canvas.create_polygon(
                center_x + 80,
                center_y - 50,
                center_x + 60,
                center_y - 10,
                center_x + 100,
                center_y - 10,
                fill=eye_color,
            )

        # Nez
        style_nez = self.style_vars["nez"].get()
        if style_nez == "Petit":
            self.canvas.create_oval(
                center_x - 20, center_y + 10, center_x + 20, center_y + 50, fill="black"
            )
        elif style_nez == "Grand":
            self.canvas.create_oval(
                center_x - 40, center_y - 10, center_x + 40, center_y + 60, fill="black"
            )
        elif style_nez == "Pointu":
            self.canvas.create_polygon(
                center_x,
                center_y - 10,
                center_x - 20,
                center_y + 60,
                center_x + 20,
                center_y + 60,
                fill="black",
            )

        # Bouche
        style_bouche = self.style_vars["bouche"].get()
        if style_bouche == "Sourire":
            self.canvas.create_arc(
                center_x - 100,
                center_y + 80,
                center_x + 100,
                center_y + 140,
                start=0,
                extent=-180,
                style=tk.ARC,
                outline="black",
                width=6,
            )
        elif style_bouche == "Droite":
            self.canvas.create_line(
                center_x - 100,
                center_y + 110,
                center_x + 100,
                center_y + 110,
                fill="black",
                width=6,
            )
        elif style_bouche == "Triste":
            self.canvas.create_arc(
                center_x - 100,
                center_y + 110,
                center_x + 100,
                center_y + 170,
                start=0,
                extent=180,
                style=tk.ARC,
                outline="black",
                width=6,
            )

    def creation_portrait(self):
        """
        fonction qui définit différentes options à cocher (radiobutton) pour chaque caractériqtique du potrait

        Returns
        -------
        None.

        """
        # Cheveux
        frame = self.frames["cheveux"]
        ttk.Label(frame, text="Style des cheveux :").pack(anchor="w")
        for option in ["Longs", "Courts"]:
            ttk.Radiobutton(
                frame,
                text=option,
                variable=self.style_vars["cheveux"],
                value=option,
                command=self.update_canvas,
            ).pack(anchor="w")

        ttk.Label(frame, text="Couleur des cheveux :").pack(anchor="w", pady=(10, 0))
        color_options = {
            "Blond très clair": "#FAEBA7",
            "Blond foncé": "#D4B157",
            "Roux": "#F47011",
            "Châtain": "#7B4E20",
            "Brun": "#29130A",
        }
        for label, hexcode in color_options.items():
            ttk.Radiobutton(
                frame,
                text=label,
                variable=self.hair_color,
                value=hexcode,
                command=self.update_canvas,
            ).pack(anchor="w")

        # Oreilles
        frame = self.frames["oreilles"]
        ttk.Label(frame, text="Forme des oreilles :").pack(anchor="w")
        for option in ["Ronde", "Carrée", "Antenne"]:
            ttk.Radiobutton(
                frame,
                text=option,
                variable=self.style_vars["oreilles"],
                value=option,
                command=self.update_canvas,
            ).pack(anchor="w")

        # Nez
        frame = self.frames["nez"]
        ttk.Label(frame, text="Forme du nez :").pack(anchor="w")
        for option in ["Petit", "Grand", "Pointu"]:
            ttk.Radiobutton(
                frame,
                text=option,
                variable=self.style_vars["nez"],
                value=option,
                command=self.update_canvas,
            ).pack(anchor="w")

        # Yeux
        frame = self.frames["yeux"]
        ttk.Label(frame, text="Forme des yeux :").pack(anchor="w")
        for option in ["Rond", "Carré", "Triangle"]:
            ttk.Radiobutton(
                frame,
                text=option,
                variable=self.style_vars["yeux_forme"],
                value=option,
                command=self.update_canvas,
            ).pack(anchor="w")

        ttk.Label(frame, text="Couleur des yeux :").pack(anchor="w", pady=(10, 0))
        for color in ["bleu", "vert", "marron", "noir"]:
            ttk.Radiobutton(
                frame,
                text=color.capitalize(),
                variable=self.eye_color,
                value=color,
                command=self.update_canvas,
            ).pack(anchor="w")

        # Bouche
        frame = self.frames["bouche"]
        ttk.Label(frame, text="Forme de la bouche :").pack(anchor="w")
        for option in ["Sourire", "Droite", "Triste"]:
            ttk.Radiobutton(
                frame,
                text=option,
                variable=self.style_vars["bouche"],
                value=option,
                command=self.update_canvas,
            ).pack(anchor="w")

        # Couleurs (peau)
        frame = self.frames["couleurs"]
        ttk.Label(frame, text="Couleur de la peau :").pack(anchor="w")
        skin_scale = tk.Scale(
            frame,
            from_=0,
            to=100,
            orient="horizontal",
            variable=self.skin_tone,
            label="Clair → Foncé",
            command=lambda e: self.update_canvas(),
            bg="#fbe8ea",
            fg="#4b2e2e",
            width=20,
            font=("Helvetica", 20),
            troughcolor="#e1a4b6",
            highlightbackground="#fbe8ea",
        )
        skin_scale.pack(fill="x", pady=10)

        btn = ttk.Button(
            frame, text="Sauvegarder son portrait robot", command=self.update_canvas
        )
        btn.pack(pady=10)

    def couleur_peau(self):
        """
        fonction qui permet d'ajuster la couleur de peau avec d'une scale
        fonction générée à l'aide d'IA (chat gpt)

        Returns
        -------
        str
            le nom de la couleur avec les paramètres rgb (red,green,blue)

        """
        t = self.skin_tone.get() / 100
        r = int((1 - t) * 245 + t * 85)
        g = int((1 - t) * 222 + t * 60)
        b = int((1 - t) * 179 + t * 40)
        return f"#{r:02x}{g:02x}{b:02x}"


if __name__ == "__main__":
    app = AvatarCreationView()
    app.mainloop()
