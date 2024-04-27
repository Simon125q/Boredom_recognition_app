import customtkinter as ctk

class AppStart(ctk.CTkFrame):
    def __init__(self, master, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.master = master
        self.initView()

    def initView(self) -> None:
        label = ctk.CTkLabel(self, text="AppStart Page")
        label.pack()
        backButton = ctk.CTkButton(self, text="Back", command=self.master.openMenu)
        backButton.pack()