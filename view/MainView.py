import tkinter as tk


class MainView(tk.Toplevel):
    def __init__(self, username, user_controller, window_controller):
        super().__init__()
        self.title("Trouver l'amour de ta vie")
        self.configure(bg="#fbe8ea")
        self.attributes("-fullscreen", True)
        self.bind("<Escape>", lambda e: self.attributes("-fullscreen", False))

        self.username = username
        self.user_controller = user_controller
        self.window_controller = window_controller

        screen_height = self.winfo_screenheight()

        font_title = ("Helvetica", int(screen_height * 0.035), "bold")
        font_button = ("Helvetica", int(screen_height * 0.025))

        # Frame principale
        main_frame = tk.Frame(self, bg="#fbe8ea")
        main_frame.pack(expand=True)

        tk.Label(
            main_frame,
            text="Bienvenue " + self.username,
            font=font_title,
            bg="#fbe8ea",
        ).pack(pady=(int(screen_height * 0.05), int(screen_height * 0.03)))

        self.find_love_button = tk.Button(
            main_frame,
            text="Trouver ton amour <3",
            font=font_button,
            bg="#e1a4b6",
            fg="white",
            relief="flat",
            command=self.open_expectations_questions_vue,
        )
        self.find_love_button.pack(pady=int(screen_height * 0.04), ipadx=10, ipady=5)

    def open_expectations_questions_vue(self):
        from view.QuestionsView import QuestionsView

        self.window_controller.go_to_window(
            self,
            QuestionsView(
                self.user_controller,
                self.window_controller,
                self.username,
                expectation_mode=True,
            ),
        )
