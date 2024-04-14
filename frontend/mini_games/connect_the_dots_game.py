from frontend.mini_games.AbstractGame import AbstractGame
import customtkinter as ctk
import random
import math


'''700x400 is center more or less'''


class Dot:
    def __init__(self, x, y, number):
        self.x = x
        self.y = y
        self.number = number


class TimerApp:
    def __init__(self, root):
        self.root = root
        self.timer_label = ctk.CTkLabel(root, text="Elapsed time: 00:00")
        self.timer_label.pack(side=ctk.TOP)

        self.seconds = 0
        self.update_timer()

    def update_timer(self):
        minutes = self.seconds // 60
        seconds = self.seconds % 60
        self.timer_label.configure(text=f"Elapsed time: \t {minutes:02d}:{seconds:02d}")
        self.seconds += 1
        self.root.after(1000, self.update_timer)


class DotsGame(AbstractGame):
    def __init__(self) -> None:
        super().__init__()
        self.info_label = None
        self.selected_point = None
        self.points = None
        self.canvas = None
        self.init_game()
        self.next_point_needed = 1
        self.timer = None
        self.all_patterns = None

    def init_game(self) -> None:
        self.root.geometry("1600x900")

        pattern_functions = [self.generate_rect_grid, self.generate_spiral, self.generate_random_dots]

        self.all_patterns = []

        for pattern_function in pattern_functions:
            pattern = pattern_function()
            self.all_patterns.append(pattern)

        self.timer = TimerApp(self.root)

        label = ctk.CTkLabel(self.root, text="Connect the dots to make ...")  # maybe add a string that has a name of
        # the dots pattern
        label.pack()

        self.info_label = ctk.CTkLabel(self.root, text="")  # Initialize info_label
        self.info_label.pack()

        self.canvas = ctk.CTkCanvas(self.root, width=1400, height=800)
        self.canvas.pack()

        self.points = self.randomise_dots()

        for dot in self.points:
            x, y = dot.x, dot.y
            self.canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="black")
            self.canvas.create_text(x, y + 15, text=str(dot.number))

        self.canvas.bind("<Button-1>", self.on_canvas_click)

    def find_closest_point(self, x, y):
        return min(self.points, key=lambda dot: ((dot.x - x) ** 2 + (dot.y - y) ** 2) ** 0.5)

    def on_canvas_click(self, event) -> None:
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
            # how the fuck do I quit this?
            # stop the timer then

        #  print(f"Selected point: {self.selected_point}")   debugger.

    def draw_line(self, dot1, dot2) -> None:
        x1, y1 = dot1.x, dot1.y
        x2, y2 = dot2.x, dot2.y
        self.canvas.create_line(x1, y1, x2, y2, fill="blue", width=2)

    def randomise_dots(self):
        return random.choice(self.all_patterns)

    @staticmethod
    def generate_rect_grid():
        center_x = 700
        center_y = 400
        grid_size = 150

        num_rows = 5
        num_cols = 5

        start_x = center_x - (num_cols // 2) * grid_size
        start_y = center_y - (num_rows // 2) * grid_size

        grid = []
        current_number = 1
        for row in range(num_rows):
            for col in range(num_cols):
                x = start_x + col * grid_size
                y = start_y + row * grid_size
                grid.append(Dot(x, y, current_number))
                current_number += 1
        return grid

    @staticmethod
    def generate_spiral():
        center_x = 700  # Fixed center x-coordinate
        center_y = 400  # Fixed center y-coordinate
        radius_increment = 18
        angle_increment = 1.2

        spiral_dots = []
        radius = 0

        current_number = 1
        for i in range(20):
            angle = i * angle_increment
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            spiral_dots.append(Dot(int(x), int(y), current_number))

            current_number += 1
            radius += radius_increment

        return spiral_dots

    @staticmethod
    def generate_random_dots():
        random_dots = []
        current_number = 1
        for _ in range(20):
            x = random.randint(200, 1200)
            y = random.randint(200, 700)
            random_dots.append(Dot(x, y, current_number))
            current_number += 1
        return random_dots

    def show(self) -> int:
        self.root.mainloop()
        points = 100

        return points


if __name__ == "__main__":
    DotsGame = DotsGame()
    DotsGame.show()
