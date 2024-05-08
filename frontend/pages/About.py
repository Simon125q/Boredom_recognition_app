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

        project_button = ctk.CTkButton(self, width=MENU_BUTTON_WIDTH, height=MENU_BUTTON_HEIGHT, text="PROJECT", font=buttonFont, command=self.show_project)
        project_button.place(relx=0.4,rely= 0.1, anchor="center")

        authors_button = ctk.CTkButton(self, width=MENU_BUTTON_WIDTH, height=MENU_BUTTON_HEIGHT, text="AUTHORS", font=buttonFont, command=self.show_authors)
        authors_button.place(relx=0.6, rely=0.1, anchor="center")

        backButton = ctk.CTkButton(self, width=MENU_BUTTON_WIDTH/2, height=MENU_BUTTON_HEIGHT/2, text="Back", font=buttonFont, command=self.master.openMenu)
        backButton.pack( side="bottom", pady=(0,10),padx = (50,0))

        self.info_label = ctk.CTkLabel(self, text = "", font = ctk.CTkFont(size = 30))
        self.info_label.place(relx= 0.5, rely = 0.5, anchor = "center")

        self.project_frame = ctk.CTkFrame(self)
        self.authors_frame = ctk.CTkFrame(self)

        # self.show_project()

    def show_project(self):
        self.project_frame.place(relx=0.5, rely=0.5, anchor="center")
        self.authors_frame.place_forget()

        for widget in self.project_frame.winfo_children():
            widget.destroy()

        project_info_label = ctk.CTkLabel(self.project_frame, text="Welcome to 2cool4you, where our top priority is keeping you on track.\nYou have a choice of several games blah blah blah", font=ctk.CTkFont(size=30))
        project_info_label.pack()

    def show_authors(self):
        self.authors_frame.place(relx=0.5, rely=0.5, anchor="center")
        self.project_frame.place_forget()

        for widget in self.authors_frame.winfo_children():
            widget.destroy()

        fonts = ctk.CTkFont(size = 15)

        info_label = ctk.CTkLabel(self.authors_frame, text = "Meet the Authors", font = ctk.CTkFont(size=30) )
        info_label.pack(side = "top")


        row1_frame = ctk.CTkFrame(self.authors_frame)
        row1_frame.pack()
        row2_frame = ctk.CTkFrame(self.authors_frame)
        row2_frame.pack()
        row3_frame = ctk.CTkFrame(self.authors_frame)
        row3_frame.pack()
        
        anastazja_info_label = ctk.CTkLabel(row1_frame, text="Anastazja Czapkowicz", font=fonts)
        anastazja_info_label.pack(side = "left",padx=20)

        szymon_info_label = ctk.CTkLabel(row1_frame, text="Szymon Omiecinski", font=fonts)
        szymon_info_label.pack(side = "left",padx=20)

        dorian_info_label = ctk.CTkLabel(row2_frame, text="Dorian Bialkowski", font=fonts)
        dorian_info_label.pack(side = "left",padx=20)

        hubert_info_label = ctk.CTkLabel(row2_frame, text="Hubert Osika", font=fonts)
        hubert_info_label.pack(side = "left",padx=20)
 
        cindy_info_label = ctk.CTkLabel(row3_frame, text="Cindy Freestone", font=fonts)
        cindy_info_label.pack(side="left", padx = 20)

        kornelia_info_label = ctk.CTkLabel(row3_frame, text="Kornelia Machnicka", font=fonts)
        kornelia_info_label.pack(side = "left",padx=20)
