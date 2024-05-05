import customtkinter as ctk
from PIL import Image
from frontend.pages.UI_settings import *
from settings import *

class About(ctk.CTkFrame):
    def __init__(self, master, **kwargs) -> None:
        super().__init__(master, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, **kwargs)
        self.master = master
        self.initView()

    def initView(self) -> None:
        labelFont = ctk.CTkFont(size=50)
        label = ctk.CTkLabel(self, text="ABOUT", font = labelFont)
        # label.pack(pady=(40)) #40 pixel brlow and above
        label.place(relx=0.2, anchor="ne")  


        buttonFont = ctk.CTkFont(size=40)

        project_button = ctk.CTkButton(self, width=MENU_BUTTON_WIDTH, height=MENU_BUTTON_HEIGHT, text="PROJECT", font=buttonFont, command=self.project)
        project_button.place(relx=0.4,rely= 0.1, anchor="center")

        authors_button = ctk.CTkButton(self, width=MENU_BUTTON_WIDTH, height=MENU_BUTTON_HEIGHT, text="AUTHORS", font=buttonFont, command=self.authors)
        authors_button.place(relx=0.6, rely=0.1, anchor="center")

        backButton = ctk.CTkButton(self, width=MENU_BUTTON_WIDTH/2, height=MENU_BUTTON_HEIGHT/2, text="Back", font=buttonFont, command=self.master.openMenu)
        backButton.pack( side="bottom", pady=(0,10),padx = (50,0))

        self.dynamic_text = ctk.CTkLabel(self, text="")  # Create a label to display dynamic text
        self.dynamic_text.place(anchor = "center", rely = 0.5, relx = 0.2)

    def project(self):
        self.dynamic_text.config(text="You clicked on the PROJECT button!")

    def authors(self):
        self.dynamic_text.config(text="You clicked on the AUTHORS button!")

