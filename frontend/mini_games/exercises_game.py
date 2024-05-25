from frontend.mini_games.AbstractGame import AbstractGame
import customtkinter as ctk
import random

'''700x400 is center more or less'''
global score


class TimerApp:
    def __init__(self, root, exercise_label, button, exercise_time):
        self.root = root
        self.exercise_label = exercise_label
        self.button = button
        self.timer_label = ctk.CTkLabel(root, text="Time for this exercise: 00:00")
        custom_font = ctk.CTkFont(family='helvetica', size=40)
        self.timer_label.configure(font=custom_font)
        self.timer_label.place(x=100, y=200)

        self.seconds = exercise_time
        self.running = True
        self.update_timer()

    def update_timer(self):
        minutes = self.seconds // 60
        seconds = self.seconds % 60
        if self.seconds >= 0:
            self.timer_label.configure(text=f"Time for this exercise: {minutes:02d}:{seconds:02d}")
        else:
            abs_seconds = abs(self.seconds)
            neg_minutes = abs_seconds // 60
            neg_seconds = abs_seconds % 60
            self.timer_label.configure(text=f"Time for this exercise: -{neg_minutes:02d}:{neg_seconds:02d}")
        if self.seconds <= 0:
            self.button.configure(state=ctk.NORMAL)
        self.seconds -= 1
        self.root.after(1000, self.update_timer)

    def stop_timer(self):
        self.running = False

    def start_timer(self):
        self.running = True
        self.update_timer()


class ExercisesGame(AbstractGame):
    def __init__(self) -> None:
        super().__init__()
        self.info_label = None
        self.button = None
        self.exercise_label = None
        self.timer = None
        self.finished_flag = False
        self.init_game()

    def init_game(self) -> None:
        global score
        dx = int(self.root.winfo_screenwidth() / 2 - 700 / 2)
        dy = int(self.root.winfo_screenheight() / 2 - 700 / 2) 
        self.root.geometry(str(700) + "x" + str(700) + f"+{dx}+{dy}") 
        self.root.update()

        exercise_name, exercise_time = self.getExerciseFromFile("frontend/mini_games/exercises.txt")

        self.exercise_label = ctk.CTkLabel(self.root, text=f"Exercise: {exercise_name}")
        custom_font = ctk.CTkFont(family='helvetica', size=40)
        self.exercise_label.configure(font=custom_font)

        self.exercise_label.place(x=350, y=300, anchor="center")

        self.button = ctk.CTkButton(self.root, text="Complete Exercise", command=self.set_finished_flag,
                                    state=ctk.DISABLED, width=300, height=75)

        self.button.place(x=200, y=350)

        self.timer = TimerApp(self.root, self.exercise_label, self.button, exercise_time)

    def set_finished_flag(self):
        self.finished_flag = True
        self.close()

    @staticmethod
    def getExerciseFromFile(file_path):
        exercises = []
        with open(file_path, 'r') as file:
            for line in file:
                exercise, time = line.strip().split(';')
                exercises.append((exercise, int(time)))
        return random.choice(exercises)

    def show(self) -> int:
        global score
        self.root.master.wait_window(self.root)
        if self.finished_flag is True:            # SCORE CALCULATION
            score = -200 + (150 - (abs(self.timer.seconds) // 2))  # initial -200, every second of delay equal "-2", with 0 delay being only -50

        return score


if __name__ == "__main__":
    ExercisesGame = ExercisesGame()
    ExercisesGame.show()
