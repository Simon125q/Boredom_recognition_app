import customtkinter as ctk
from PIL import Image
from frontend.pages.UI_settings import *
from settings import *

class Menu(ctk.CTkFrame):
    def __init__(self, master, **kwargs) -> None:
        super().__init__(master, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, **kwargs)
        self.master = master
        self.initView()

    def initView(self) -> None:
        sideImgData = Image.open("assets/tower.jpg")
        sideImg = ctk.CTkImage(light_image=sideImgData, dark_image=sideImgData, size=(SIDE_IMG_WIDTH, WINDOW_HEIGHT))
        sideImgLabel = ctk.CTkLabel(self, text="", image=sideImg)
        sideImgLabel.pack(expand=True, side="left")
        nameFont = ctk.CTkFont(size=75, weight="bold")
        buttonFont = ctk.CTkFont(size=30)
        app_name = ctk.CTkLabel(self, text=APP_NAME, font=nameFont)
        app_name.pack(pady = 80)
        start_button = ctk.CTkButton(self, width=MENU_BUTTON_WIDTH, height=MENU_BUTTON_HEIGHT, text="START", font=buttonFont, command=self.master.startApp)
        start_button.pack(pady = 20, padx = (WINDOW_WIDTH - (SIDE_IMG_WIDTH + MENU_BUTTON_WIDTH)) / 2)
        stats_button = ctk.CTkButton(self, width=MENU_BUTTON_WIDTH, height=MENU_BUTTON_HEIGHT, text="STATISTICS", font=buttonFont, command=self.master.openStats)
        stats_button.pack(pady = 20)
        sett_button = ctk.CTkButton(self, width=MENU_BUTTON_WIDTH, height=MENU_BUTTON_HEIGHT, text="SETTINGS", font=buttonFont, command=self.master.openSettings)
        sett_button.pack(pady = 20)
        about_button = ctk.CTkButton(self, width=MENU_BUTTON_WIDTH, height=MENU_BUTTON_HEIGHT, text="ABOUT", font=buttonFont, command=self.master.openAbout)
        about_button.pack(pady = 20)

 