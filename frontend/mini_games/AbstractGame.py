import customtkinter as ctk
from abc import ABC, abstractmethod
from settings import *


class AbstractGame(ABC):
    def __init__(self) -> None:
        self.init_root()

    def init_root(self) -> None:
        self.root = ctk.CTkToplevel()
        self.root.geometry(str(WINDOW_WIDTH) + "x" + str(WINDOW_HEIGHT))
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