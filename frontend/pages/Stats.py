from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import customtkinter as ctk

class Stats(ctk.CTkFrame):
    def __init__(self, master, data, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.master = master
        self.data = data
        self.getData()
        self.initView()

    def initView(self) -> None:
        self.createGraphFrame()
        self.createSideCanvas()

    def createSideCanvas(self) -> None:
        self.sideFrame = ctk.CTkFrame(self, width=400, height=750)
        self.sideFrame.pack(side="left", padx=0)
        self.sideCanvas = ctk.CTkCanvas(self.sideFrame, width=400, height=750, borderwidth=0)
        self.sideCanvas.pack(expand=True, side="left", padx=0)
        sideImgData = Image.open("assets/levelBar.png")
        self.sideImg = ImageTk.PhotoImage(sideImgData, size=(400,750))
        self.sideCanvas.background = self.sideImg
        self.sideCanvas.create_image(0, 0, image=self.sideImg, anchor="nw")
        backButton = ctk.CTkButton(self, width=200, height=50, text="Back", font=ctk.CTkFont(size=30), command=self.master.openMenu)
        self.sideCanvas.create_window(100, 670, anchor="nw", window=backButton)
        self.sideCanvas.create_text(200, 170, fill="white", font=('Arial', 80, 'bold'), text=str(self.level))
        self.sideCanvas.create_text(200, 365, fill="black", font=('Arial', 30, 'normal'), text=str(self.points))
        self.sideCanvas.create_text(200, 475, fill="black", font=('Arial', 30, 'normal'), text=str(f"{self.hours}h {self.minutes}min"))
        print(self.sideCanvas)

    def createGraphFrame(self) -> None:
        self.graphFrame = ctk.CTkFrame(self)
        self.graphFrame.pack(expand=True, fill="both", side="right")
        barFig, barAx = self.barGraph()
        barFig.patch.set_facecolor("#333333")
        barGraphCanvas = FigureCanvasTkAgg(barFig, self.graphFrame)
        barGraphCanvas.draw()
        barGraphCanvas.get_tk_widget().pack(fill="x", expand=True, side="top")

    def getData(self) -> None:
        self.points = self.data["points"].sum()
        time = self.data["time_spend"].sum()
        self.level = self.points // 1000 + 1 
        self.hours = time // 60
        self.minutes = (time - self.hours * 60) 

    def barGraph(self) -> set:
        
        plt.rcParams["axes.prop_cycle"] = plt.cycler(
        color=["#5e87f5", "#f0420f"])
        COLOR = 'white'
        plt.rcParams['text.color'] = COLOR
        plt.rcParams['axes.labelcolor'] = COLOR
        plt.rcParams['xtick.color'] = COLOR
        plt.rcParams['ytick.color'] = COLOR

        dates = self.data["date"].tail(7).tolist()
        values = {
            'time [min]': self.data["time_spend"].tail(7).tolist(),
            "points": self.data["points"].tail(7).tolist()
        }

        x = np.arange(len(dates))  # the label locations
        width = 0.2  # the width of the bars
        multiplier = 0
        
        fig, ax = plt.subplots(layout='constrained')

        for attribute, measurement in values.items():
            offset = width * multiplier
            rects = ax.bar(x + offset, measurement, width, label=attribute)
            ax.bar_label(rects, padding=3)
            multiplier += 1

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('')
        ax.set_title('')
        ax.set_facecolor("#333333")
        ax.set_xticks(x + width, dates)
        ax.legend(loc='upper right', ncols=3, facecolor="#303030")

        return (fig, ax)
