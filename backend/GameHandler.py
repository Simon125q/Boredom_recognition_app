from frontend.mini_games.connect_the_dots_game import DotsGame
from backend.MaxSizeQueue import MaxSizeQueue

class GameHandler:
    def __init__(self) -> None:
        self.games = list()
        self.initGames()
        self.initMarkContainers()

    def initGames(self) -> None:
        DotsGame = DotsGame()
        self.games.append(DotsGame)
    
    def initMarkContainers(self) -> None:
        self.earQueue = MaxSizeQueue(500)
        self.marQueue = MaxSizeQueue(500)
        self.poseQueue = MaxSizeQueue(700)

    def handleGame(self) -> int:
        mouth = self.marQueue.getMax()
        eyes = self.earQueue.getMax()
        pose = self.poseQueue.getMax()
        print(mouth, eyes, pose)
        return 0

    def get_data(self, pose: str, pose_prob: float, ear: float, eyes: str, mar: float, mouth: str) -> None:
        self.earQueue.add(eyes)
        self.marQueue.add(mouth)
        self.poseQueue.add(pose)
        if len(self.earQueue) > 200 and len(self.marQueue) > 200 and len(self.poseQueue) > 200:
            self.handleGame()


