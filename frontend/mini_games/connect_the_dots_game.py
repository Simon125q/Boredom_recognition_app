from frontend.mini_games.AbstractGame import AbstractGame
import customtkinter as ctk
import random
import frontend.mini_games.dot_patterns as dot_patterns
from settings import *


'''700x400 is center more or less'''
global score


class TimerApp:
    def __init__(self, root):
        self.root = root
        self.timer_label = ctk.CTkLabel(root, text="Elapsed time: 00:00")
        self.timer_label.pack(side=ctk.TOP)

        self.seconds = 0
        self.running = True
        self.update_timer()

    def update_timer(self):
        if self.running:
            minutes = self.seconds // 60
            seconds = self.seconds % 60
            self.timer_label.configure(text=f"Elapsed time: \t {minutes:02d}:{seconds:02d}")
            self.seconds += 1
            self.root.after(1000, self.update_timer)

    def stop_timer(self):
        self.running = False

    def start_timer(self):
        self.running = True
        self.update_timer()


class DotsGame(AbstractGame):
    def __init__(self) -> None:
        super().__init__()

    def restart(self) -> None:
        self.info_label = None
        self.selected_point = None
        self.points = None
        self.canvas = None
        self.init_game()
        self.next_point_needed = 1
        self.timer = TimerApp(self.root)
        self.all_patterns = None
        

    def init_game(self) -> None:
        dx = int(self.root.winfo_screenwidth() / 2 - 1600 / 2)
        dy = int(self.root.winfo_screenheight() / 2 - 900 / 2) 
        self.root.geometry(str(1600) + "x" + str(900) + f"+{dx}+{dy}") 
        self.timer = None

        # adding more patterns here:
        pattern_functions = dot_patterns.populate_patterns()

        label = ctk.CTkLabel(self.root, text="Connect the dots to make a pattern")
        label.pack()

        self.all_patterns = []

        for pattern in pattern_functions:
            self.all_patterns.append(pattern)

        self.timer = TimerApp(self.root)

        self.info_label = ctk.CTkLabel(self.root, text="")
        self.info_label.pack()

        self.canvas = ctk.CTkCanvas(self.root, width=1400, height=800, bg="#868686")
        self.canvas.pack()

        self.points = self.randomise_dots()

        for dot in self.points:
            x, y = dot.x, dot.y
            self.canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="black")
            self.canvas.create_text(x, y + 15, text=str(dot.number))

        self.canvas.bind("<Motion>", self.on_canvas_click)

    def find_closest_point(self, x, y):
        return min(self.points, key=lambda dot: ((dot.x - x) ** 2 + (dot.y - y) ** 2) ** 0.5)

    def on_canvas_click(self, event) -> None:
        global score
        x, y = event.x, event.y

        closest_dot = self.find_closest_point(x, y)

        if ((closest_dot.x - x) ** 2 + (closest_dot.y - y) ** 2) ** 0.5 < 10:
            if closest_dot.number == self.next_point_needed:
                if self.selected_point is not None:
                    self.draw_line(self.selected_point, closest_dot)
                self.selected_point = closest_dot
                self.info_label.configure(text="")
                self.next_point_needed += 1
            else:
                self.info_label.configure(text="Invalid selection. Try again.")

        if self.next_point_needed == len(self.points) + 1:
            self.info_label.configure(text="Congratulations! You've connected all dots.")
            self.timer.running = False  # SCORE CALCULATION
            score = -200 + (200 - (abs(self.timer.seconds) * 5))   # base -200, players with e.g. 10 seconds get (-200 + (200 - (10s * 5)) = 150
            self.close()   # assume avg time of completion 10 s with only hover, granting the faster more or less 150 as in every game

    def draw_line(self, dot1, dot2) -> None:
        x1, y1 = dot1.x, dot1.y
        x2, y2 = dot2.x, dot2.y
        self.canvas.create_line(x1, y1, x2, y2, fill="blue", width=4)

    def randomise_dots(self):
        return random.choice(self.all_patterns)

    def show(self) -> int:
        self.restart()
        self.root.master.wait_window(self.root)
        return score


if __name__ == "__main__":
    DotsGame = DotsGame()
    DotsGame.show()
