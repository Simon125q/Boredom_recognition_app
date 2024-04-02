import customtkinter as ctk
from settings import *

class App:
    def __init__(self) -> None:
        self.root = ctk.CTk()
        self.set_default_look()

    def set_default_look(self) -> None:
        self.root.geometry(str(WINDOW_WIDTH) + "x" + str(WINDOW_HEIGHT))
        self.root.title(TITLE)
        

    def run(self) -> None:
        self.root.mainloop()



if __name__ == "__main__":
    app = App()
    app.run()