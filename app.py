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
        if SETTINGS["gamesEnable"]["DotsGame"]:
            self.games.append(GameType.DOTS)
        if SETTINGS["gamesEnable"]["Excercises"]:
            self.games.append(GameType.EXCERCISE)
        if SETTINGS["gamesEnable"]["Snake"]:
            self.games.append(GameType.SNAKE)
        if SETTINGS["gamesEnable"]["Memory"]:
            self.games.append(GameType.MEMORY)
        if SETTINGS["gamesEnable"]["Alarm"]:
            self.games.append(GameType.ALARM)
        if SETTINGS["gamesEnable"]["TicTacToe"]:
            self.games.append(GameType.TICTACTOE)
                  
    def set_default_look(self) -> None:
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.close)
        dx = int(self.winfo_screenwidth() / 2 - WINDOW_WIDTH / 2)
        dy = int(self.winfo_screenheight() / 2 - WINDOW_HEIGHT / 2) 
        self.geometry(str(WINDOW_WIDTH) + "x" + str(WINDOW_HEIGHT) + f"+{dx}+{dy}")
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
        points = game.show()
        print(points)
        
    def checkGameStatus(self) -> None:
        if self.detector.getGameStatus():
            self.startRandomGame()
            self.detector.resetGameStatus()
            self.detector.gameHandler.startTimer()

    def close(self) -> None:
        self.detector.closeCamera()
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
            