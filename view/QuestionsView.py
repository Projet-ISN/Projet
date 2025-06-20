import tkinter as tk
from tkinter import *

from controller.UserController import UserController
from controller.WindowController import WindowController
from model.SurveyAnswers import SurveyAnswers
from util.json_utils import load_questions, load_user_as_person, get_usernames
from view.MainView import MainView
from view.ResultsView import ResultsView

QUESTIONS_PATH = "data/questions.json"
questions = load_questions(QUESTIONS_PATH)


class QuestionsView(tk.Toplevel):
    def __init__(
        self,
        user_controller: UserController,
        window_controller: WindowController,
        username: str,
        question_index=0,
        answers: dict = {},
        expectation_mode=False,
    ):
        super().__init__()

        self.title("Pour en apprendre plus sur vous")
        self.attributes("-fullscreen", True)
        self.configure(bg="#fbe8ea")
        self.bind("<Escape>", lambda e: self.attributes("-fullscreen", False))
        self.bind("<Return>", self.go_to_next_question)

        self.user_controller = user_controller
        self.window_controller = window_controller
        self.username = username
        self.index = question_index
        self.answers = answers
        self.expectation_mode = expectation_mode
        self.question = questions[question_index]

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        relative_padding = int(screen_height * 0.05)
        scale_length = int(screen_width * 0.6)

        # Question Text
        self.text = tk.Label(
            self,
            text=self.question["question"],
            font=("Helvetica", int(screen_height * 0.025), "bold"),
            wraplength=int(screen_width * 0.8),
            justify="center",
            bg="#fbe8ea",
            fg="#4b2e2e",
        )
        self.text.pack(pady=relative_padding)

        self.middle = tk.Frame(self, bg="#fbe8ea")
        self.middle.pack(pady=int(relative_padding / 2))

        self.importance = tk.Label(
            self.middle,
            text="Importance de cette question selon vous :",
            font=("Helvetica", int(screen_height * 0.022)),
            bg="#fbe8ea",
            fg="#4b2e2e",
        )
        if self.expectation_mode:
            self.importance.pack(pady=10)

        self.sc1 = tk.Scale(
            self.middle,
            from_=1,
            to=10,
            orient="horizontal",
            length=scale_length,
            sliderlength=30,
            width=20,
            font=("Helvetica", int(screen_height * 0.02)),
            bg="#fbe8ea",
            fg="#4b2e2e",
            troughcolor="#e1a4b6",
            highlightbackground="#fbe8ea",
            activebackground="#fbe8ea",
        )
        if self.expectation_mode:
            self.sc1.pack(pady=10)

        self.frame = tk.Frame(self, bg="#fbe8ea")
        self.frame.pack()

        font_size = int(screen_height * 0.022)

        if self.question["choix"] == "multiple":
            self.choix1 = tk.BooleanVar()
            self.choix2 = tk.BooleanVar()
            self.choix3 = tk.BooleanVar()
            self.choix4 = tk.BooleanVar()

            options = self.question["options"]
            variables = [self.choix1, self.choix2, self.choix3, self.choix4]
            for i, option in enumerate(options[:4]):
                cb = tk.Checkbutton(
                    self.frame,
                    text=option,
                    variable=variables[i],
                    bg="#fbe8ea",
                    fg="#4b2e2e",
                    font=("Helvetica", font_size),
                    activebackground="#fbe8ea",
                    selectcolor="#ffe6ec",
                )
                cb.pack(pady=10)

        elif self.question["choix"] == "unique":
            self.choix = tk.IntVar()
            self.choix.set(0)

            for idx, option in enumerate(self.question["options"]):
                rb = tk.Radiobutton(
                    self.frame,
                    text=option,
                    variable=self.choix,
                    value=idx + 1,
                    bg="#fbe8ea",
                    fg="#4b2e2e",
                    font=("Helvetica", font_size),
                    activebackground="#fbe8ea",
                    selectcolor="#ffe6ec",
                )
                rb.pack(pady=10)

        self.nav_frame = tk.Frame(self, bg="#fbe8ea")
        self.nav_frame.pack(pady=int(screen_height * 0.1))

        btn_font = ("Helvetica", int(screen_height * 0.02))
        btn_padx = int(screen_width * 0.04)
        btn_pady = int(screen_height * 0.015)

        self.prec = tk.Button(
            self.nav_frame,
            text="← Précédent",
            font=btn_font,
            bg="#e1a4b6",
            fg="white",
            relief="flat",
            padx=btn_padx,
            pady=btn_pady,
            command=self.go_to_previous_question,
        )
        self.prec.pack(side="left", padx=int(screen_width * 0.1))

        self.suiv = tk.Button(
            self.nav_frame,
            text="Suivant →",
            font=btn_font,
            bg="#e1a4b6",
            fg="white",
            relief="flat",
            padx=btn_padx,
            pady=btn_pady,
            command=self.go_to_next_question,
        )
        self.suiv.pack(side="right", padx=int(screen_width * 0.1))

    def go_to_previous_question(self):
        if self.index > 0:
            self.index -= 1
            QuestionsView(
                self.user_controller,
                self.window_controller,
                self.username,
                self.index,
                expectation_mode=self.expectation_mode,
            )
            self.destroy()

    def go_to_next_question(self, event=None):
        if self.question["choix"] == "unique":
            self.answers[self.index] = self.choix.get()

        if self.question["choix"] == "multiple":
            self.answers[self.index] = [
                self.choix1.get(),
                self.choix2.get(),
                self.choix3.get(),
                self.choix4.get(),
            ]

        if self.expectation_mode:
            self.answers[self.index] = {
                "answer": self.answers[self.index],
                "importance": self.sc1.get(),
            }

        if self.index < len(questions) - 1:
            self.index += 1
            QuestionsView(
                self.user_controller,
                self.window_controller,
                self.username,
                self.index,
                self.answers,
                expectation_mode=self.expectation_mode,
            )
            self.destroy()
        else:
            self.finish_survey()

    def finish_survey(self):
        survey_answers = SurveyAnswers(self.username, self.answers)

        if self.expectation_mode:
            self.user_controller.add_users_expectations(survey_answers)
            result = self.calculate_result()
            self.window_controller.go_to_window(self, ResultsView(result))
        else:
            self.user_controller.add_users_survey_answers(survey_answers)
            self.window_controller.go_to_window(
                self,
                MainView(self.username, self.user_controller, self.window_controller),
            )
        print(f"Réponses enregistrées pour {self.username}")

    def calculate_result(self):
        results = []
        person = load_user_as_person(self.username)

        usernames = get_usernames()
        candidates = []

        for username in usernames:
            if username != self.username:
                person2 = load_user_as_person(username)
                candidates.append({"username": username, "person": person2})

        for candidate in candidates:
            if candidate["person"] is None:
                continue
            compatibilite = person.compatibilite(candidate["person"])
            results.append(
                {"username": candidate["username"], "compatibility": compatibilite}
            )

        results.sort(key=lambda x: x["compatibility"], reverse=True)
        return results[:3]
