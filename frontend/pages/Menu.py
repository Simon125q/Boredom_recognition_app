import customtkinter as ctk
from frontend.pages.UI_settings import *
from settings import *

class Menu(ctk.CTkFrame):
    def __init__(self, master, **kwargs) -> None:
        super().__init__(master, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, **kwargs)
        self.master = master
        self.initView()

    def initView(self) -> None:
        
        app_name = ctk.CTkLabel(self, text=APP_NAME)
        app_name.pack(pady = 40)
        start_button = ctk.CTkButton(self, width=MENU_BUTTON_WIDTH, height=MENU_BUTTON_HEIGHT, text="START", command=self.master.startApp)
        start_button.pack(pady = 20)
        stats_button = ctk.CTkButton(self, text="STATISTICS", command=self.master.openStats)
        stats_button.pack(pady = 20)
        sett_button = ctk.CTkButton(self, text="SETTINGS", command=self.master.openSettings)
        sett_button.pack(pady = 20)
        about_button = ctk.CTkButton(self, text="ABOUT", command=self.master.openAbout)
        about_button.pack(pady = 20)

 