from random import choice
from frontend.mini_games.connect_the_dots_game import DotsGame
#from frontend.mini_games.exercises_game import ExercisesGame 
import customtkinter as ctk
from settings import *
from frontend.Detector import Detector
import warnings
import threading
warnings.filterwarnings("ignore")


class App:
    def __init__(self) -> None:
        self.detector = Detector()
        self.root = ctk.CTk()
        self.games = list()
        self.running = True
        self.set_default_look()
        self.initGames()

    def initGames(self) -> None:
        if CONNECT_DOTS_ENABLE:
            self.games.append("dots")
        if EXCERCISE_ENABLE:
            self.games.append("excercise")

    def set_default_look(self) -> None:
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.root.geometry(str(WINDOW_WIDTH) + "x" + str(WINDOW_HEIGHT))
        self.root.title(TITLE)
        self.menu()

    def start_camera(self) -> None:
        detector_thread = threading.Thread(target=self.detector.start)
        detector_thread.start()

    def startRandomGame(self) -> None:
        randGame = choice(self.games)
        if randGame == "dots":
            print("new game")
            game = DotsGame()
        game.show()
        
    def checkGameStatus(self) -> None:
        if self.detector.getGameStatus():
            self.startRandomGame()
            self.detector.resetGameStatus()
            self.detector.gameHandler.startTimer()

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

    def close(self) -> None:
        self.root.quit()
        self.running = False

    def run(self) -> None:
        while self.running:
            self.root.update_idletasks()
            self.root.update()
            self.checkGameStatus() 
            

if __name__ == "__main__":
    app = App()
    app.run()
            