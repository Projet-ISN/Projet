import tkinter as tk
from tkinter import ttk

# This import would be from your project structure.
from view.QuestionsView import QuestionsView


class AvatarCreationView(tk.Toplevel):
    def __init__(self, user_controller, window_controller, username: str):
        super().__init__()

        self.title("Portrait Robot")
        self.attributes("-fullscreen", True)
        self.configure(bg="#fbe8ea")
        self.bind("<Escape>", lambda e: self.attributes("-fullscreen", False))

        self.user_controller = user_controller
        self.window_controller = window_controller
        self.username = username

        # --- Responsive Sizing Setup ---
        screen_height = self.winfo_screenheight()
        screen_width = self.winfo_screenwidth()
        font_tab = ("Helvetica", int(screen_height * 0.02))
        font_widget = ("Helvetica", int(screen_height * 0.018))
        main_padding = int(screen_width * 0.02)
        widget_padding = int(screen_height * 0.01)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TNotebook", background="#fbe8ea", borderwidth=0)
        style.configure(
            "TNotebook.Tab",
            background="#e1a4b6",
            foreground="white",
            font=font_tab,
            padding=widget_padding,
        )
        style.configure("TFrame", background="#fbe8ea")
        style.configure(
            "TLabel", background="#fbe8ea", font=font_widget, foreground="#4b2e2e"
        )
        style.configure(
            "TRadiobutton", background="#fbe8ea", font=font_widget, foreground="#4b2e2e"
        )
        style.configure(
            "TButton", background="#e1a4b6", foreground="white", font=font_widget
        )

        # --- Grid Layout Configuration for Responsiveness ---
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(
            1, weight=1
        )  # Using 1:1 weight ratio to give them equal space preference

        # On construit le canva qui où sera l'avatar - NO fixed width/height
        self.canvas = tk.Canvas(self, bg="#fbe8ea", highlightthickness=0)
        self.canvas.grid(
            row=0, column=1, padx=main_padding, pady=main_padding, sticky="nsew"
        )

        # Notebook avec les différents onglets
        self.notebook = ttk.Notebook(self)
        self.notebook.grid(
            row=0, column=0, sticky="nsew", padx=main_padding, pady=main_padding
        )

        self.frames = {}
        categories = ["Cheveux", "Oreilles", "Nez", "Yeux", "Bouche", "Couleurs"]
        for cat in categories:
            frame = ttk.Frame(self.notebook, padding=widget_padding * 2)
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

        # CRUCIAL: Bind the redraw to the canvas resize event
        self.canvas.bind("<Configure>", lambda e: self.update_canvas())

    def update_canvas(self):
        """
        Fonction qui met à jour le canva en ÉCHELONNANT le dessin original
        pour qu'il s'adapte à la taille actuelle du canva.
        """
        self.canvas.delete("all")

        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        if canvas_width <= 1 or canvas_height <= 1:
            return

        # Original dimensions from your hardcoded values
        original_width = 1000
        original_height = 1000

        # Calculate scaling factors
        scale_x = canvas_width / original_width
        scale_y = canvas_height / original_height

        # Use an average scale for line widths to prevent distortion
        avg_scale = (scale_x + scale_y) / 2.0
        scaled_line_width = max(1, int(6 * avg_scale))

        # The original center point
        center_x = 500
        center_y = 500

        skin_color = self.couleur_peau()
        hair_color = self.hair_color.get()

        # Tête
        self.canvas.create_oval(
            (center_x - 200) * scale_x,
            (center_y - 200) * scale_y,
            (center_x + 200) * scale_x,
            (center_y + 200) * scale_y,
            fill=skin_color,
            outline="black",
        )

        # Cheveux
        style_cheveux = self.style_vars["cheveux"].get()
        if style_cheveux == "Longs":
            self.canvas.create_rectangle(
                (center_x - 200) * scale_x,
                (center_y - 240) * scale_y,
                (center_x + 200) * scale_x,
                (center_y - 180) * scale_y,
                fill=hair_color,
            )
        elif style_cheveux == "Courts":
            self.canvas.create_rectangle(
                (center_x - 100) * scale_x,
                (center_y - 200) * scale_y,
                (center_x + 100) * scale_x,
                (center_y - 170) * scale_y,
                fill=hair_color,
            )

        # Oreilles
        style_oreilles = self.style_vars["oreilles"].get()
        if style_oreilles == "Ronde":
            self.canvas.create_oval(
                (center_x - 240) * scale_x,
                (center_y - 50) * scale_y,
                (center_x - 200) * scale_x,
                (center_y + 50) * scale_y,
                fill="black",
            )
            self.canvas.create_oval(
                (center_x + 200) * scale_x,
                (center_y - 50) * scale_y,
                (center_x + 240) * scale_x,
                (center_y + 50) * scale_y,
                fill="black",
            )
        elif style_oreilles == "Carrée":
            self.canvas.create_rectangle(
                (center_x - 240) * scale_x,
                (center_y - 50) * scale_y,
                (center_x - 200) * scale_x,
                (center_y + 50) * scale_y,
                fill="black",
            )
            self.canvas.create_rectangle(
                (center_x + 200) * scale_x,
                (center_y - 50) * scale_y,
                (center_x + 240) * scale_x,
                (center_y + 50) * scale_y,
                fill="black",
            )
        elif style_oreilles == "Antenne":
            self.canvas.create_line(
                (center_x - 230) * scale_x,
                (center_y - 50) * scale_y,
                (center_x - 230) * scale_x,
                (center_y - 120) * scale_y,
                fill="black",
                width=scaled_line_width,
            )
            self.canvas.create_line(
                (center_x + 230) * scale_x,
                (center_y - 50) * scale_y,
                (center_x + 230) * scale_x,
                (center_y - 120) * scale_y,
                fill="black",
                width=scaled_line_width,
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
                (center_x - 100) * scale_x,
                (center_y - 50) * scale_y,
                (center_x - 60) * scale_x,
                (center_y - 10) * scale_y,
                fill=eye_color,
            )
            self.canvas.create_oval(
                (center_x + 60) * scale_x,
                (center_y - 50) * scale_y,
                (center_x + 100) * scale_x,
                (center_y - 10) * scale_y,
                fill=eye_color,
            )
        elif form_yeux == "Carré":
            self.canvas.create_rectangle(
                (center_x - 100) * scale_x,
                (center_y - 50) * scale_y,
                (center_x - 60) * scale_x,
                (center_y - 10) * scale_y,
                fill=eye_color,
            )
            self.canvas.create_rectangle(
                (center_x + 60) * scale_x,
                (center_y - 50) * scale_y,
                (center_x + 100) * scale_x,
                (center_y - 10) * scale_y,
                fill=eye_color,
            )
        elif form_yeux == "Triangle":
            self.canvas.create_polygon(
                (center_x - 80) * scale_x,
                (center_y - 50) * scale_y,
                (center_x - 100) * scale_x,
                (center_y - 10) * scale_y,
                (center_x - 60) * scale_x,
                (center_y - 10) * scale_y,
                fill=eye_color,
            )
            self.canvas.create_polygon(
                (center_x + 80) * scale_x,
                (center_y - 50) * scale_y,
                (center_x + 60) * scale_x,
                (center_y - 10) * scale_y,
                (center_x + 100) * scale_x,
                (center_y - 10) * scale_y,
                fill=eye_color,
            )

        # Nez
        style_nez = self.style_vars["nez"].get()
        if style_nez == "Petit":
            self.canvas.create_oval(
                (center_x - 20) * scale_x,
                (center_y + 10) * scale_y,
                (center_x + 20) * scale_x,
                (center_y + 50) * scale_y,
                fill="black",
            )
        elif style_nez == "Grand":
            self.canvas.create_oval(
                (center_x - 40) * scale_x,
                (center_y - 10) * scale_y,
                (center_x + 40) * scale_x,
                (center_y + 60) * scale_y,
                fill="black",
            )
        elif style_nez == "Pointu":
            self.canvas.create_polygon(
                (center_x) * scale_x,
                (center_y - 10) * scale_y,
                (center_x - 20) * scale_x,
                (center_y + 60) * scale_y,
                (center_x + 20) * scale_x,
                (center_y + 60) * scale_y,
                fill="black",
            )

        # Bouche
        style_bouche = self.style_vars["bouche"].get()
        if style_bouche == "Sourire":
            self.canvas.create_arc(
                (center_x - 100) * scale_x,
                (center_y + 80) * scale_y,
                (center_x + 100) * scale_x,
                (center_y + 140) * scale_y,
                start=0,
                extent=-180,
                style=tk.ARC,
                outline="black",
                width=scaled_line_width,
            )
        elif style_bouche == "Droite":
            self.canvas.create_line(
                (center_x - 100) * scale_x,
                (center_y + 110) * scale_y,
                (center_x + 100) * scale_x,
                (center_y + 110) * scale_y,
                fill="black",
                width=scaled_line_width,
            )
        elif style_bouche == "Triste":
            self.canvas.create_arc(
                (center_x - 100) * scale_x,
                (center_y + 110) * scale_y,
                (center_x + 100) * scale_x,
                (center_y + 170) * scale_y,
                start=0,
                extent=180,
                style=tk.ARC,
                outline="black",
                width=scaled_line_width,
            )

    def creation_portrait(self):
        """
        Cette fonction reste la même, car elle configure juste les widgets.
        Les polices sont déjà responsives grâce à la configuration du style dans __init__.
        """
        screen_height = self.winfo_screenheight()
        font_scale = ("Helvetica", int(screen_height * 0.015))
        widget_padding = int(screen_height * 0.01)

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
        ttk.Label(frame, text="Couleur des cheveux :").pack(
            anchor="w", pady=(widget_padding, 0)
        )
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

        # Oreilles, Nez, Yeux, Bouche... (pas de changements nécessaires ici)
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
        ttk.Label(frame, text="Couleur des yeux :").pack(
            anchor="w", pady=(widget_padding, 0)
        )
        for color in ["bleu", "vert", "marron", "noir"]:
            ttk.Radiobutton(
                frame,
                text=color.capitalize(),
                variable=self.eye_color,
                value=color,
                command=self.update_canvas,
            ).pack(anchor="w")

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

        # Couleurs (peau) - la scale est aussi rendue responsive
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
            width=int(screen_height * 0.02),
            font=font_scale,
            troughcolor="#e1a4b6",
            highlightbackground="#fbe8ea",
        )
        skin_scale.pack(fill="x", pady=widget_padding)

        btn = ttk.Button(
            frame, text="Sauvegarder son portrait robot", command=self.go_to_questions
        )
        btn.pack(pady=widget_padding)

    def couleur_peau(self):
        t = self.skin_tone.get() / 100
        r = int((1 - t) * 245 + t * 85)
        g = int((1 - t) * 222 + t * 60)
        b = int((1 - t) * 179 + t * 40)
        return f"#{r:02x}{g:02x}{b:02x}"

    def go_to_questions(self):
        self.save_avatar()
        self.window_controller.go_to_window(
            self,
            QuestionsView(self.user_controller, self.window_controller, self.username),
        )

    def save_avatar(self):
        # TODO: Implement the logic to save the avatar creation data
        pass


if __name__ == "__main__":
    # --- Mock classes for standalone testing ---
    class MockController:
        def go_to_window(self, old_window, new_window):
            print(f"Switching from {old_window.title()} to {new_window.title()}")
            old_window.destroy()

    class MockQuestionsView(tk.Toplevel):
        def __init__(self, user_controller, window_controller, username: str):
            super().__init__()
            self.title("Questions")
            tk.Label(self, text=f"This is the next screen for {username}").pack(
                padx=100, pady=100
            )
            self.attributes("-fullscreen", True)

    # Replace the real view with the mock for testing
    QuestionsView = MockQuestionsView

    root = tk.Tk()
    root.withdraw()
    app = AvatarCreationView(MockController(), MockController(), "TestUser")
    app.mainloop()
