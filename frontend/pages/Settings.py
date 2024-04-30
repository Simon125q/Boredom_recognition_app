import json
import customtkinter as ctk


class Settings(ctk.CTkFrame):
    def __init__(self, master, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.master = master
        self.camera_enabled = 0
        self.min_time_break = "40"
        self.entry = None
        self.toggle_descriptions = ["DotsGame", "Exercises", "Snake", "Memory", "TicTacToe", "Alarm"]
        self.toggle_states = {}
        self.clear_content()
        self.load_settings()
        self.initView()

    def load_settings(self):
        try:
            with open("mySettings.json", "r") as f:
                settings = json.load(f)
                self.toggle_states = settings.get("gamesEnable", {})
                self.camera_enabled = settings.get("camera", 0)
                self.min_time_break = settings.get("breakTime", 0)
        except FileNotFoundError:
            self.toggle_states = {description: 0 for description in self.toggle_descriptions}
            self.camera_enabled = 0

    def save_settings(self):
        settings = {"gamesEnable": self.toggle_states, "camera": self.camera_enabled, "breakTime": self.min_time_break}
        with open("mySettings.json", "w") as f:
            json.dump(settings, f, indent=4)

    def initView(self) -> None:
        label = ctk.CTkLabel(self, text="Settings", font=("Helvetica", 75, "bold"))
        label.pack(anchor="nw", padx=40, pady=20)

        toggle_descriptions = ["DotsGame", "Exercises", "Snake", "Memory", "TicTacToe", "Alarm"]
        for description in toggle_descriptions:
            toggle_frame = ctk.CTkFrame(self)
            toggle_frame.pack(anchor="nw", padx=40,  pady=20)

            initial_state = self.toggle_states.get(description, 0)
            initial_text = "ON" if initial_state == 1 else "OFF"

            toggle_button = ctk.CTkButton(toggle_frame, text=initial_text, font=("Helvetica", 15, "bold"))
            toggle_button.configure(command=lambda btn=toggle_button, desc=description: self.toggle(btn, desc))
            toggle_button.pack(side="left")

            description_label = ctk.CTkLabel(toggle_frame, text=description, font=("Helvetica", 25, "bold"))
            description_label.pack(side="left", padx=5)

        self.setup_camera()
        self.setup_time_break()

        backButton = ctk.CTkButton(self, text="Exit", font=("Helvetica", 35, "bold"), command=self.just_exit)
        backButton.place(anchor="center", relx=0.8, rely=0.9)

        save_button = ctk.CTkButton(self, text="Save & Exit", font=("Helvetica", 35, "bold"), command=self.save_and_exit)
        save_button.place(anchor="center", relx=0.2, rely=0.9)

    def setup_camera(self):
        initial_camera_state = self.camera_enabled
        initial_camera_text = "ON" if initial_camera_state == 1 else "OFF"

        camera_button = ctk.CTkButton(self, text=initial_camera_text, font=("Helvetica", 15, "bold"))
        camera_button.configure(command=lambda btn=camera_button: self.toggle_camera(btn))
        camera_button.place(relx=0.9, rely=0.15, anchor="center")

        camera_label = ctk.CTkLabel(self, text="Show Camera", font=("Helvetica", 25, "bold"))
        camera_label.place(anchor="center", relx=0.75, rely=0.15)

    def setup_time_break(self):
        self.entry = ctk.CTkEntry(self)
        self.entry.insert(0, self.min_time_break)
        self.entry.place(anchor="center", relx=0.9, rely=0.3)

        time_label = ctk.CTkLabel(self, text="Min time between games (sec)", font=("Helvetica", 25, "bold"))
        time_label.place(anchor="center", relx=0.68, rely=0.3)

    def toggle(self, button, description):
        current_state = self.toggle_states.get(description, 0)
        new_state = 1 - current_state
        self.toggle_states[description] = new_state
        new_text = "ON" if new_state == 1 else "OFF"
        button.configure(text=new_text)

    def toggle_camera(self, btn):
        self.camera_enabled = 1 - self.camera_enabled
        new_text = "ON" if self.camera_enabled == 1 else "OFF"
        btn.configure(text=new_text)

    def clear_content(self):
        for widget in self.winfo_children():
            widget.destroy()

    def just_exit(self):
        self.load_settings()
        self.clear_content()
        self.initView()
        self.master.openMenu()

    def save_and_exit(self):
        self.min_time_break = int(self.entry.get())
        self.save_settings()
        self.master.openMenu()
