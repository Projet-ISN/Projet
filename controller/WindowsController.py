class WindowsController:
    def __init__(self):
        pass

    def go_to_window(self, source, destination):
        source.destroy()
        destination.focus_force()