import customtkinter as ctk
from abc import ABC, abstractmethod
from settings import *
import pygame


class AbstractGame(ABC):
    def __init__(self) -> None:
        self.init_root()
        pygame.mixer.init()
        pygame.mixer.music.load("assets/interface-3.mp3")
        pygame.mixer.music.play()

    def init_root(self) -> None:
        self.root = ctk.CTkToplevel()
        dx = int(self.root.winfo_screenwidth() / 2 - WINDOW_WIDTH / 2)
        dy = int(self.root.winfo_screenheight() / 2 - WINDOW_HEIGHT / 2) 
        self.root.geometry(str(WINDOW_WIDTH) + "x" + str(WINDOW_HEIGHT) + f"+{dx}+{dy}")       
        self.root.title(TITLE)
        self.root.lift()  # lift window on top
        self.root.attributes("-topmost", True)  # stay on top
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.root.resizable(False, False)
        self.root.grab_set()  # make other windows not clickable

    def close(self) -> None:
        self.root.grab_release()
        self.root.destroy()
        self.running = False
    

    @abstractmethod
    def show(self) -> int:
        pass