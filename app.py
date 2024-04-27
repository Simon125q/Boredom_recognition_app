from random import choice
from frontend.mini_games.connect_the_dots_game import DotsGame
from frontend.mini_games.exercises_game import ExercisesGame 
from frontend.pages.Menu import Menu
from frontend.pages.About import About
from frontend.pages.Stats import Stats
from frontend.pages.Settings import Settings
from frontend.pages.AppStart import AppStart
import customtkinter as ctk
from settings import *
from frontend.Detector import Detector
import warnings
import threading
warnings.filterwarnings("ignore")


class App(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        self.detector = Detector()
        self.games = list()
        self.running = True
        self.initFrames()
        self.set_default_look()
        self.initGames()

    def initGames(self) -> None:
        if CONNECT_DOTS_ENABLE:
            self.games.append(GameType.DOTS)
        if EXCERCISE_ENABLE:
            self.games.append(GameType.EXCERCISE)
        if SNAKE_ENABLE:
            self.games.append(GameType.SNAKE)
        if MEMORY_ENABLE:
            self.games.append(GameType.MEMORY)
        if ALARM_ENABLE:
            self.games.append(GameType.ALARM)

    def set_default_look(self) -> None:
        self.protocol("WM_DELETE_WINDOW", self.close)
        self.geometry(str(WINDOW_WIDTH) + "x" + str(WINDOW_HEIGHT))
        self.title(TITLE)
        self.openMenu()

    def start_camera(self) -> None:
        detector_thread = threading.Thread(target=self.detector.start)
        detector_thread.start()

    def startRandomGame(self) -> None:
        randGame = choice(self.games)
        if randGame == GameType.DOTS:
            game = DotsGame()
        elif randGame == GameType.EXCERCISE:
            game = ExercisesGame()
        game.show()
        
    def checkGameStatus(self) -> None:
        if self.detector.getGameStatus():
            self.startRandomGame()
            self.detector.resetGameStatus()
            self.detector.gameHandler.startTimer()

    def close(self) -> None:
        self.quit()
        self.running = False
    
    def initFrames(self) -> None:
        self.menu = Menu(self)
        self.about = About(self)
        self.stats = Stats(self)
        self.settings = Settings(self)
        self.appStart = AppStart(self)

    def startApp(self) -> None:
        self.hideFrames()
        self.start_camera()
        self.appStart.pack()

    def openStats(self) -> None:
        self.hideFrames()
        self.stats.pack()
    
    def openSettings(self) -> None:
        self.hideFrames()
        self.settings.pack() 

    def openAbout(self) -> None:
        self.hideFrames()
        self.about.pack()

    def openMenu(self) -> None:
        self.hideFrames()
        self.menu.pack()

    def hideFrames(self) -> None:
        self.menu.pack_forget()
        self.about.pack_forget()
        self.stats.pack_forget()
        self.settings.pack_forget()
        self.appStart.pack_forget()

    def run(self) -> None:
        while self.running:
            self.update_idletasks()
            self.update()
            self.checkGameStatus()
            

if __name__ == "__main__":
    app = App()
    app.run()
            