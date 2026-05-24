# import .*
import customtkinter as ctk
# from .* import .*

class Livro(ctk.CTkButton):
    def __init__(self, master, image):
        super().__init__(
            master=master, 
            text="",
            image=image,
            width=88,
            height=112,
            fg_color="transparent",
            hover_color=("#F0F0F0", "#191919"),
            cursor="hand2"
        )

        