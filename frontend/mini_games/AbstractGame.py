import customtkinter as ctk
from abc import ABC, abstractmethod
from settings import *

class AbstractGame(ABC):
    def __init__(self) -> None:
        self.root = ctk.CTk()
        self.root.geometry(str(WINDOW_WIDTH) + "x" + str(WINDOW_HEIGHT))
        self.root.title(TITLE)

    @abstractmethod
    def show(self) -> int:
        pass