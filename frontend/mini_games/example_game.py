from frontend.mini_games.AbstractGame import AbstractGame
import customtkinter as ctk

class ExampleGame(AbstractGame):
    def __init__(self) -> None:
        super().__init__()
        self.init_game()

    def init_game(self) -> None:
        label = ctk.CTkLabel(self.root, text="-- This is example game --")
        label.pack()

    def show(self) -> int:
        self.root.mainloop()
        points = 100

        return points
    

if __name__ == "__main__":
    exampleGame = ExampleGame()
    exampleGame.show()