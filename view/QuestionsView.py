# -*- coding: utf-8 -*-
"""
Created on Wed Jun  4 20:04:26 2025

@author: stani
"""
import tkinter as tk
from tkinter import *
from controller.UserController import UserController
from controller.WindowController import WindowController
from model.SurveyAnswers import SurveyAnswers
from util.json_utils import load_questions
from view.MainView import MainView
from view.ResultsView import ResultsView

QUESTIONS_PATH = "data/questions.json"

questions = load_questions(QUESTIONS_PATH)


class QuestionsView(tk.Toplevel):
    def __init__(
        self,
        user_controller: UserController,
        window_controller: WindowController,
        username,
        question_index=0,
        answers: dict = {},
        expectation_mode=False,
    ):
        super().__init__()

        self.title("Pour en apprendre plus sur vous")
        self.attributes("-fullscreen", True)  # ouverture en plein écran par défaut
        self.configure(bg="#fbe8ea")  # couleur de fond
        self.bind("<Escape>", lambda e: self.attributes("-fullscreen", False))

        self.user_controller = user_controller
        self.window_controller = window_controller
        self.username = username
        self.index = question_index
        self.answers = answers
        self.expectation_mode = expectation_mode
        self.question = questions[question_index]

        # affichage de la question
        self.text = tk.Label(
            self,
            text=self.question["question"],
            font=("Helvetica", 22, "bold"),
            wraplength=1000,
            justify="center",
            bg="#fbe8ea",
            fg="#4b2e2e",
        )
        self.text.pack(pady=70)

        self.middle = tk.Frame(self, bg="#fbe8ea")
        self.middle.pack(pady=30)

        self.importance = tk.Label(
            self.middle,
            text="Importance de cette question selon vous :",
            font=("Helvetica", 20),
            bg="#fbe8ea",
            fg="#4b2e2e",
        )

        if self.expectation_mode:
            self.importance.pack(pady=20)

        self.sc1 = tk.Scale(
            self.middle,
            from_=1,
            to=10,
            orient="horizontal",
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

        if expectation_mode:
            self.sc1.pack(pady=15)

        self.frame = tk.Frame(self, bg="#fbe8ea")
        self.frame.pack()
        # si la question est à choix multiple
        if self.question["choix"] == "multiple":
            self.choix1 = tk.BooleanVar()
            self.choix2 = tk.BooleanVar()
            self.choix3 = tk.BooleanVar()
            self.choix4 = tk.BooleanVar()

            self.cb1 = tk.Checkbutton(
                self.frame,
                text=self.question["options"][0],
                variable=self.choix1,
                bg="#fbe8ea",
                fg="#4b2e2e",
                font=("Helvetica", 18),
                activebackground="#fbe8ea",
                selectcolor="#ffe6ec",
            )
            self.cb1.pack(pady=10)
            self.cb2 = tk.Checkbutton(
                self.frame,
                text=self.question["options"][1],
                variable=self.choix2,
                bg="#fbe8ea",
                fg="#4b2e2e",
                font=("Helvetica", 18),
                activebackground="#fbe8ea",
                selectcolor="#ffe6ec",
            )
            self.cb2.pack(pady=10)
            self.cb3 = tk.Checkbutton(
                self.frame,
                text=self.question["options"][2],
                variable=self.choix3,
                bg="#fbe8ea",
                fg="#4b2e2e",
                font=("Helvetica", 18),
                activebackground="#fbe8ea",
                selectcolor="#ffe6ec",
            )
            self.cb3.pack(pady=10)
            self.cb4 = tk.Checkbutton(
                self.frame,
                text=self.question["options"][3],
                variable=self.choix4,
                bg="#fbe8ea",
                fg="#4b2e2e",
                font=("Helvetica", 18),
                activebackground="#fbe8ea",
                selectcolor="#ffe6ec",
            )
            self.cb4.pack(pady=50)

        # sinon si elle est à choix unique
        elif self.question["choix"] == "unique":
            self.choix = tk.IntVar()
            self.choix.set(0)

            self.rb1 = tk.Radiobutton(
                self.frame,
                text=self.question["options"][0],
                variable=self.choix,
                value=1,
                bg="#fbe8ea",
                fg="#4b2e2e",
                font=("Helvetica", 18),
                activebackground="#fbe8ea",
                selectcolor="#ffe6ec",
            )
            self.rb1.pack(pady=10)
            self.rb2 = tk.Radiobutton(
                self.frame,
                text=self.question["options"][1],
                variable=self.choix,
                value=2,
                bg="#fbe8ea",
                fg="#4b2e2e",
                font=("Helvetica", 18),
                activebackground="#fbe8ea",
                selectcolor="#ffe6ec",
            )
            self.rb2.pack(pady=10)
            if len(self.question["options"]) > 2:
                self.rb3 = tk.Radiobutton(
                    self.frame,
                    text=self.question["options"][2],
                    variable=self.choix,
                    value=3,
                    bg="#fbe8ea",
                    fg="#4b2e2e",
                    font=("Helvetica", 18),
                    activebackground="#fbe8ea",
                    selectcolor="#ffe6ec",
                )
                self.rb3.pack(pady=10)

            if len(self.question["options"]) > 3:
                self.rb4 = tk.Radiobutton(
                    self.frame,
                    text=self.question["options"][3],
                    variable=self.choix,
                    value=4,
                    bg="#fbe8ea",
                    fg="#4b2e2e",
                    font=("Helvetica", 18),
                    activebackground="#fbe8ea",
                    selectcolor="#ffe6ec",
                )
                self.rb4.pack(pady=10)

        self.nav_frame = tk.Frame(self, bg="#fbe8ea")
        self.nav_frame.pack(pady=120)

        # boutons précédent et suivant
        self.prec = tk.Button(
            self.nav_frame,
            text="← Précédent",
            font=("Helvetica", 14),
            bg="#e1a4b6",
            fg="white",
            relief="flat",
            padx=30,
            pady=10,
            command=self.go_to_previous_question,
        )
        self.prec.pack(side="left", padx=100, pady=70)

        self.suiv = tk.Button(
            self.nav_frame,
            text="Suivant →",
            font=("Helvetica", 14),
            bg="#e1a4b6",
            fg="white",
            relief="flat",
            padx=30,
            pady=10,
            command=self.go_to_next_question,
        )
        self.suiv.pack(side="right", padx=100, pady=70)

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

    def go_to_next_question(self):
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
                expectation_mode=self.expectation_mode,
            )
            self.destroy()
        elif self.index == len(questions) - 1:
            self.finish_survey()

    def finish_survey(self):
        survey_answers = SurveyAnswers(self.username, self.answers)

        if self.expectation_mode:
            self.user_controller.add_users_expectations(survey_answers.answers)
            self.window_controller.go_to_window(self, ResultsView([], []))
        else:
            self.user_controller.add_users_survey_answers(survey_answers)
            self.window_controller.go_to_window(
                self,
                MainView(self.username, self.user_controller, self.window_controller),
            )

        print(f"Réponses enregistrées pour {self.username}")
