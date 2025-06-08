from tkinter import Tk


class WindowsController:
    def __init__(self):
        pass

    def go_to_window(self, source, destination):
        print(source.title(), "->", destination.title())

        # Si on appelle destroy() sur la fenêtre principale (Tk), cela ferme l'application.
        if isinstance(source, Tk):
            source.withdraw()
        else:
            source.destroy()

        destination.focus_force()