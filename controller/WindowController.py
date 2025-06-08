from tkinter import Tk


class WindowController:
    """
    Classe qui gère la transition entre les différentes fenêtres de l'application.
    """
    # C'est équivalent à un constructeur vide mais c'est plus clair.
    def __init__(self):
        pass

    def go_to_window(self, source, destination):
        """
        Permet de changer de fenêtre dans l'application.
        """
        # Si on appelle destroy() sur la fenêtre principale (Tk), cela ferme l'application.
        if isinstance(source, Tk):
            source.withdraw()
        else:
            source.destroy()

        destination.focus_force()
