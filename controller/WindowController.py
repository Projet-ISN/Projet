from tkinter import Tk


class WindowController:
    # C'est équivalent à un constructeur vide mais c'est plus clair.
    def __init__(self):
        pass

    def go_to_window(self, source, destination):
        # Si on appelle destroy() sur la fenêtre principale (Tk), cela ferme l'application.
        if isinstance(source, Tk):
            source.withdraw()
        else:
            source.destroy()

        destination.focus_force()
