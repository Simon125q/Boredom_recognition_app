import customtkinter as ctk
from settings import *
from frontend.Detector import Detector
from frontend.mini_games.example_game import ExampleGame


class App:
    def __init__(self) -> None:
        self.detector = Detector()
        self.root = ctk.CTk()
        self.exampleGame = ExampleGame()
        self.set_default_look()

    def set_default_look(self) -> None:
        self.root.geometry(str(WINDOW_WIDTH) + "x" + str(WINDOW_HEIGHT))
        self.root.title(TITLE)
        self.menu()

    def start_camera(self) -> None:
        self.detector.start()
        
    def menu(self) -> None:
        start_button = ctk.CTkButton(self.root, text="Start", command=self.start_camera)
        start_button.pack()
        game_button = ctk.CTkButton(self.root, text="Example Game", command=self.exampleGame.show)
        game_button.pack()

    def run(self) -> None:
        self.root.mainloop()



if __name__ == "__main__":
    app = App()
    app.run()