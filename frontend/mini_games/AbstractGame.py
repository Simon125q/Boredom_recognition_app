import customtkinter as ctk
from abc import ABC, abstractmethod
from settings import *


class AbstractGame(ABC):
    def __init__(self) -> None:
        self.init_root()

    def init_root(self) -> None:
        self.root = ctk.CTk()
        self.root.geometry(str(WINDOW_WIDTH) + "x" + str(WINDOW_HEIGHT))
        self.root.title(TITLE)
        self.running = True
    #    self.root.protocol("WM_DELETE_WINDOW", self.close)

    def close(self) -> None:
        self.root.quit()
        self.running = False
    

    @abstractmethod
    def show(self) -> int:
        pass