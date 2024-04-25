from settings import *
import time
from frontend.mini_games.connect_the_dots_game import DotsGame
from backend.MaxSizeQueue import MaxSizeQueue
from random import choice

class GameHandler:
    def __init__(self) -> None:
        self.gameStatus = False
        self.games = list()
        self.initMarkContainers()
        self.startTimer()

    
    def initMarkContainers(self) -> None:
        self.earQueue = MaxSizeQueue(500)
        self.marQueue = MaxSizeQueue(500)
        self.poseQueue = MaxSizeQueue(700)

    def startTimer(self) -> None:
        self.startTime = time.time()

    def checkTime(self, target_seconds) -> bool:
        if time.time() - self.startTime < target_seconds:
            return False
        else:
            return True
    
    def getGameStatus(self) -> bool:
        return self.gameStatus
    
    def resetGameStatus(self) -> None:
        self.gameStatus = False
        
    def handleGame(self) -> None:
        mouth = self.marQueue.getMax(40)
        eyes = self.earQueue.getMax(50)
        pose = self.poseQueue.getMax(250)
        print(mouth, eyes, pose)
        if mouth[0] == 'open' or eyes[0] in ["closed", "squinted"] or pose[0] == "half-lie":
            print("game")
            self.gameStatus = True
            #game = choice(self.games)
            #game.show()
            self.startTimer()

    def get_data(self, pose: str, pose_prob: float, ear: float, eyes: str, mar: float, mouth: str) -> None:
        self.earQueue.add(eyes)
        self.marQueue.add(mouth)
        self.poseQueue.add(pose)
        timeUp = self.checkTime(TIME_BETWEEN_GAMES)
        if timeUp:
            self.handleGame()


