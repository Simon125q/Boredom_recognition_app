from frontend.mini_games.AbstractGame import AbstractGame
import customtkinter as ctk
import random
from time import sleep

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 150
SPACE_SIZE = 33
BODY_PARTS = 1
SNAKE_COLOUR = '#008000'
FOOD_COLOUR = 'red'
BACKGROUND_COLOUR = '#848482'
WINNING_SCORE = 15


class Snake:
    def __init__(self, canvas):
        self.snake_body = BODY_PARTS
        self.coords = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coords.append([0, 0])

        for x, y in self.coords:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOUR, tag="snake")
            self.squares.append(square)


class Food:
    def __init__(self, canvas):

        x = random.randint(0, int(GAME_WIDTH/SPACE_SIZE-1)) * SPACE_SIZE
        y = random.randint(0, int(GAME_HEIGHT/SPACE_SIZE-1)) * SPACE_SIZE

        self.coords = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOUR, tag="food")

class SnakeGame(AbstractGame):
    def __init__(self) -> None:
        super().__init__()
        #self.init_game()

    def restart(self) -> None:
        self.return_score = 0
        global direction 
        direction = 'down'
        global score
        score = 0
        ctk.CTkLabel(self.root, text=f'Collect {WINNING_SCORE} points', font=('Arial', 40))
        self.label = ctk.CTkLabel(self.root, text=f"Points: {score}/{WINNING_SCORE}", font=('Arial', 40))
        self.label.pack()

        self.canvas = ctk.CTkCanvas(self.root, bg=BACKGROUND_COLOUR, height=GAME_HEIGHT, width=GAME_WIDTH)
        self.canvas.pack()
        #self.root.update()

        root_width = self.root.winfo_width()
        root_height = self.root.winfo_height()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = int((screen_width / 2 - root_width / 2))
        y = int((screen_height / 2 - root_height / 2))

        self.root.geometry(f'{root_width}x{root_height}+{x}+{y}')

        self.root.bind('<Left>', lambda event: self.change_direction('left'))
        self.root.bind('<Right>', lambda event: self.change_direction('right'))
        self.root.bind('<Up>', lambda event: self.change_direction('up'))
        self.root.bind('<Down>', lambda event: self.change_direction('down'))

        snake = Snake(self.canvas)
        food = Food(self.canvas)
        self.next_turn(snake, food)


    def next_turn(self, snake, food):
        x, y = snake.coords[0]
        global direction
        if direction == "up":
            y -= SPACE_SIZE
        elif direction == "down":
            y += SPACE_SIZE
        elif direction == "left":
            x -= SPACE_SIZE
        elif direction == "right":
            x += SPACE_SIZE

        snake.coords.insert(0, (x, y))

        square = self.canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOUR)

        snake.squares.insert(0, square)

        if x == food.coords[0] and y == food.coords[1]:
            global score
            score += 1
            self.label.configure(text=f"Points: {score}/{WINNING_SCORE}")

            self.canvas.delete("food")

            food = Food(self.canvas)

        else:
            del snake.coords[-1]

            self.canvas.delete(snake.squares[-1])

            del snake.squares[-1]

        if self.check_collision(snake):
            self.game_over()
        elif score == WINNING_SCORE:
            self.win()
        else:
            self.root.after(SPEED, self.next_turn, snake, food)

    def change_direction(self, new_direction):
        global direction
        if new_direction == 'left':
            if direction != "right":
                direction = new_direction
        elif new_direction == 'right':
            if direction != "left":
                direction = new_direction
        elif new_direction == 'up':
            if direction != "down":
                direction = new_direction
        elif new_direction == 'down':
            if direction != "up":
                direction = new_direction

    def check_collision(self, snake):
        x, y = snake.coords[0]

        if x < 0 or x >= GAME_WIDTH:
            return True
        elif y < 0 or y >= GAME_HEIGHT:
            return True

        for body_part in snake.coords[1:]:
            if x == body_part[0] and y == body_part[1]:
                return True

        return False

    def game_over(self):
        global score
        self.canvas.delete("all")
        self.canvas.create_text((self.canvas.winfo_width()/2, self.canvas.winfo_height()/2)
                        , font=("Arial", 69), text="YOU LOST", fill="red", tag="game_over")
        if score >= WINNING_SCORE // 2:
            self.return_score = 35
        else:
            self.return_score = 0
        self.close()

    def win(self):
        self.canvas.delete("all")
        self.canvas.create_text((self.canvas.winfo_width() / 2, self.canvas.winfo_height() / 2)
                        , font=("Arial", 69), text="YOU WON", fill="gold", tag="game_over")
        self.return_score = 100
        self.close()

    def show(self) -> int:
        self.restart()
        self.root.master.wait_window(self.root)
        return self.return_score 


