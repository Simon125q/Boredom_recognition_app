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
        app_name = ctk.CTkLabel(self.root, text=APP_NAME)
        app_name.pack(pady = 40)
        start_button = ctk.CTkButton(self.root, text="Start", command=self.start_camera)
        start_button.pack(pady = 20)
        stats_button = ctk.CTkButton(self.root, text="Statistics")
        stats_button.pack(pady = 20)
        sett_button = ctk.CTkButton(self.root, text="Settings")
        sett_button.pack(pady = 20)
        about_button = ctk.CTkButton(self.root, text="About")
        about_button.pack(pady = 20)

    def run(self) -> None:
        self.root.mainloop()



if __name__ == "__main__":
    app = App()
    app.run()