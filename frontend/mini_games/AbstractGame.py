import customtkinter as ctk
from abc import ABC, abstractmethod

class AbstractGame(ABC):
    def __init__(self) -> None:
        self.root = ctk.CTk()

    @abstractmethod
    def show(self) -> int:
        pass