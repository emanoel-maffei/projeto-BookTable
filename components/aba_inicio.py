# import .*
import customtkinter as ctk
# from .* import .*
from customtkinter import CTkFont
from PIL import Image

class AbaInicio(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label_titulo = ctk.CTkLabel(
            master=self,
            text="Aba - Inicio",
            font=CTkFont(
                size=24,
                family="Arial"
            )
        )
        self.label_titulo.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )