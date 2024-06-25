from frontend.mini_games.AbstractGame import AbstractGame
import customtkinter as ctk
import random
from time import sleep


class MemoryGame(AbstractGame):
    def __init__(self) -> None:
        super().__init__()
        print("init")

        self.firstChoice = None
        self.secondChoice = None
        self.symbols = list("AABBCCDDEEFFGGHH")
        self.buttons = {}
        self.pairs = 0
        self.finished = False
        random.shuffle(self.symbols)

    def restart(self) -> None:
        self.create_grid(4, 4)

    def create_grid(self, rows, cols):
        for ro in range(rows):
            frame = ctk.CTkFrame(self.root)
            frame.pack(side="top", fill="x", expand=True)
            for co in range(cols):
                self.buttons[(ro, co)] = ctk.CTkButton(frame, text="", width=80, height=80,
                                       command=lambda r=ro, c=co: self.reveal_symbol(r, c) )
                self.buttons[(ro, co)].pack(side="left", fill="both", expand=True)

    def reveal_symbol(self, row, column):
        print(self.symbols)
        print(self.buttons.keys())
        button = self.buttons[(row, column)]
        index = row * 4 + column
        button.configure(text=self.symbols[index], state="disabled")

        if not self.firstChoice:
            self.firstChoice = (row, column)
        elif not self.secondChoice:
            self.secondChoice = (row, column)
            self.root.after(500, self.check_match)


    def check_match(self):
        print("checking matches")
        first_row, first_column = self.firstChoice
        second_row, second_column = self.secondChoice

        first_symbol = self.symbols[(first_row * 4 + first_column)]
        second_symbol = self.symbols[(second_row * 4 + second_column)]

        if first_symbol == second_symbol:
            self.buttons[(first_row, first_column)].configure(state="disabled", fg_color="#4CAF50")
            self.buttons[(second_row, second_column)].configure(state="disabled", fg_color="#4CAF50")
            self.pairs += 1
        else:
            self.buttons[(first_row, first_column)].configure(text='', state="normal")
            self.buttons[(second_row, second_column)].configure(text='', state="normal")

        self.firstChoice = None
        self.secondChoice = None
        if self.pairs == 8:
            self.finished = True
            self.close()


    def show(self) -> int:
        #self.play_again()
        self.restart()
        print("show")
        self.root.master.wait_window(self.root)
        print("show 2")
        return 150