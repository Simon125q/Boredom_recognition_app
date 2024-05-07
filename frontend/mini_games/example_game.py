from frontend.mini_games.AbstractGame import AbstractGame
import customtkinter as ctk

class ExampleGame(AbstractGame):
    def __init__(self) -> None:
        super().__init__()
        self.score = 100

    def init_game(self) -> None:
        label = ctk.CTkLabel(self.root, text="-- This is example game --")
        label.pack()

    def show(self) -> int:
        self.init_game()
        self.root.master.wait_window(self.root)
        return self.score
    

if __name__ == "__main__":
    exampleGame = ExampleGame()
    exampleGame.show()