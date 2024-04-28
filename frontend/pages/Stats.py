from PIL import Image, ImageTk
import pandas as pd
import customtkinter as ctk

class Stats(ctk.CTkFrame):
    def __init__(self, master, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.master = master
        self.getData()
        self.initView()

    def initView(self) -> None:
        self.createSideCanvas()
        self.createGraphFrame()

    def createSideCanvas(self) -> None:

        self.sideCanvas = ctk.CTkCanvas(self, width=400, height=750, borderwidth=0)
        self.sideCanvas.pack(expand=True, side="left")
        sideImgData = Image.open("assets/levelBar.png")
        self.sideImg = ImageTk.PhotoImage(sideImgData, size=(400,750))
        self.sideCanvas.background = self.sideImg
        self.sideCanvas.create_image(0, 0, image=self.sideImg, anchor="nw")
        backButton = ctk.CTkButton(self, text="Back", command=self.master.openMenu)
        self.sideCanvas.create_window(200 - 70, 700, anchor="nw", window=backButton)
        self.sideCanvas.create_text(200, 170, fill="white", font=('Arial', 80, 'bold'), text=str(self.level))
        self.sideCanvas.create_text(200, 365, fill="black", font=('Arial', 30, 'normal'), text=str(self.points))
        self.sideCanvas.create_text(200, 475, fill="black", font=('Arial', 30, 'normal'), text=str(f"{self.hours}h {self.minutes}min"))

    def createGraphFrame(self) -> None:
        self.graphFrame = ctk.CTkFrame(self)
        self.graphFrame.pack(expand=True, fill="both", side="right")

    def getData(self) -> None:
        #self.data = pd.read_csv("userData.csv")
        self.points = 3234
        time = 4589
        self.level = self.points // 1000 + 1 
        self.hours = time // 3600
        self.minutes = (time - self.hours * 3600) // 60 

