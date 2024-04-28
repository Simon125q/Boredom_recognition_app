from PIL import Image
import customtkinter as ctk

class Stats(ctk.CTkFrame):
    def __init__(self, master, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.master = master
        self.initView()

    def initView(self) -> None:
        sideImgData = Image.open("assets/levelBar.png")
        sideImg = ctk.CTkImage(sideImgData, size=(400,750))
        sideImgLabel = ctk.CTkLabel(self, text="", image=sideImg)
        sideImgLabel.pack(expand=True, side="left")
        label = ctk.CTkLabel(self, text="Statistics Page")
        label.pack()
        backButton = ctk.CTkButton(self, text="Back", command=self.master.openMenu)
        backButton.pack()