from settings import *
import time
from frontend.mini_games.connect_the_dots_game import DotsGame
from backend.MaxSizeQueue import MaxSizeQueue
from random import choice

class GameHandler:
    def __init__(self) -> None:
        self.games = list()
        self.initGames()
        self.initMarkContainers()
        self.startTimer()

    def initGames(self) -> None:
        if CONNECT_DOTS_ENABLE:
            self.dotsGame = DotsGame()
            self.games.append(self.dotsGame)
    
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

    def handleGame(self) -> None:
        mouth = self.marQueue.getMax(50)
        eyes = self.earQueue.getMax(100)
        pose = self.poseQueue.getMax(250)
        print(mouth, eyes, pose)
        if mouth[0] == 'open' or eyes[0] in ["closed", "squinted"] or pose[0] == "half-lie":
            print("game")
            TimeToRunGame = True
            #game = choice(self.games)
            #game.show()
            self.startTimer()

    def get_data(self, pose: str, pose_prob: float, ear: float, eyes: str, mar: float, mouth: str) -> None:
        self.earQueue.add(eyes)
        self.marQueue.add(mouth)
        self.poseQueue.add(pose)
        timeUp = self.checkTime(TIME_BETWEEN_GAMES)
        if timeUp and len(self.earQueue) > 200 and len(self.marQueue) > 200 and len(self.poseQueue) > 200:
            self.handleGame()


