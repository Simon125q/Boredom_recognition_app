from frontend.mini_games.AbstractGame import AbstractGame
import customtkinter as ctk
import pygame


class AlarmGame(AbstractGame):
    def __init__(self) -> None:
        super().__init__()
        self.init_game()


    def init_game(self) -> None:
        dx = int(self.root.winfo_screenwidth() / 2 - 700 / 2)
        dy = int(self.root.winfo_screenheight() / 2 - 700 / 2) 
        self.root.geometry(str(700) + "x" + str(700) + f"+{dx}+{dy}") 
        self.root.update()

        custom_font = ctk.CTkFont(family='helvetica', size=60)
        self.label = ctk.CTkLabel(self.root, text="Alarm!")
        self.label.configure(font=custom_font)
        self.label.place(x=350, y=170, anchor="center")

        self.turn_off_button = ctk.CTkButton(self.root, text="Turn Off", command=self.turn_off_alarm, width=300, height=75)
        self.turn_off_button.place(x=200, y=500)
        self.turn_off_button.configure(font=custom_font)

        self.alarm_sound = "alarm.mp3"

        self.schedule_alarm()


    def schedule_alarm(self):
        self.remaining_time = 30
        self.timer_label = ctk.CTkLabel(self.root, text="Time left: 60 seconds")
        self.timer_label.place(x=350, y=350, anchor="center")
        custom_font = ctk.CTkFont(family='helvetica', size=60)
        self.timer_label.configure(font=custom_font)
        self.update_timer()

        
    def update_timer(self):
        time_str = f"Time left: {self.remaining_time:02d} seconds"
        self.timer_label.configure(text=time_str)
        if self.remaining_time > 0:
            self.remaining_time -= 1
            self.root.after(1000, self.update_timer)
        else:
            self.play_alarm()

    def play_alarm(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.alarm_sound)
        pygame.mixer.music.play()

    def turn_off_alarm(self):
        self.turn_off_button.configure(state=ctk.DISABLED)
        pygame.mixer.music.stop()
        self.close()

    def show(self) -> int:
        self.root.master.wait_window(self.root)  # SCORE CALCULATION
        return -50  # ??? idk how would that work, so... assume best case


if __name__ == "__main__":
    AlarmGame = AlarmGame()
    AlarmGame.show()