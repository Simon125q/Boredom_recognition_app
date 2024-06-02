import customtkinter as ctk
import time


class TimerFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.start_time = None
        self.paused_time = None
        self.elapsed_time = 0
        self.timer_running = False
        self.timer_id = None
        self.initButtons()


    def initButtons(self):
        self.timer_label = ctk.CTkLabel(self, text="00:00:00", font=("helvetica", 200))
        self.timer_label.pack(padx=60, pady=60)

        self.start_button = ctk.CTkButton(self, text="Start", command=self.start_timer,font=("Helvetica", 40), width=200, height=50)
        self.start_button.pack(pady=20)

        self.pause_button = ctk.CTkButton(self, text="Pause", command=self.pause_timer, state="disabled",  font=("Helvetica", 40), width=200, height=50)
        self.pause_button.pack(pady=20)

        self.resume_button = ctk.CTkButton(self, text="Resume", command=self.resume_timer, font=("Helvetica", 40), width=200, height=50)
        self.resume_button.pack_forget()

        self.finish_button = ctk.CTkButton(self, text="Finish", command=self.finish_timer, font=("Helvetica", 40), width=200, height=50)
        self.finish_button.pack_forget()

        self.pack(fill="both", expand=True)


    def start_timer(self):
        self.start_button.pack_forget()
        self.pause_button.pack(pady=20)
        self.pause_button.configure(state="normal")
        self.start_time = time.time() - self.elapsed_time
        self.timer_running = True
        self.update_timer()


    def pause_timer(self):
        self.pause_button.pack_forget()
        self.resume_button.pack(pady=20)
        self.finish_button.pack(pady=20)
        self.paused_time = time.time()
        self.elapsed_time = self.paused_time - self.start_time
        self.timer_running = False
        if self.timer_id:
            self.after_cancel(self.timer_id)
            self.timer_id = None


    def resume_timer(self):
        self.resume_button.pack_forget()
        self.finish_button.pack_forget()
        self.pause_button.pack(pady=20)
        self.start_time = time.time() - self.elapsed_time
        self.timer_running = True
        self.update_timer()

   
    def finish_timer(self):
        self.timer_running = False
        if self.timer_id:
            self.after_cancel(self.timer_id)
            self.timer_id = None
        self.master.updateTime(self.elapsed_time)
        self.elapsed_time = 0
        self.timer_label.configure(text="00:00:00")
        self.start_button.pack(pady=20)
        self.pause_button.pack_forget()
        self.resume_button.pack_forget()
        self.finish_button.pack_forget()
        self.master.openMenu()


    def update_timer(self):
        if self.timer_running:
            self.elapsed_time = time.time() - self.start_time
            minutes, seconds = divmod(self.elapsed_time, 60)
            hours, minutes = divmod(minutes, 60)
            self.timer_label.configure(text="{:02d}:{:02d}:{:02d}".format(int(hours), int(minutes), int(seconds)))
            self.timer_id = self.after(1000, self.update_timer)
            

class AppStart(ctk.CTkFrame):
    def __init__(self, master, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.master = master
        self.initView()

    def initView(self) -> None:
        self.timer_frame = TimerFrame(self)
        self.timer_frame.pack()

    def updateTime(self, elapsed_time):
        minutes_spent = int(elapsed_time // 60)
        self.master.timeSpend += minutes_spent

    def openMenu(self):
        self.master.openMenu()