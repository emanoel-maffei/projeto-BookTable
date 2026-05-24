# import .*
import customtkinter as ctk
# from .* import .*
from customtkinter import CTkFont
from CTkMessagebox import CTkMessagebox

class Livro(ctk.CTkButton):
    def __init__(self, master, cod_livro, titulo, capa, subtitulo=""):
        super().__init__(
            master=master, 
            text="",
            image=capa,
            width=88,
            height=112,
            fg_color="transparent",
            bg_color=("#FFFFFF", "#000000"),
            hover_color=("#F0F0F0", "#191919"),
            cursor="hand2",
            command=self.click
        )

        self.cod_livro = cod_livro
        self.titulo = titulo
        self.subtitulo = subtitulo

    def click(self):
        CTkMessagebox(
            title="Dados do livro",
            message=f"""
                Código do Livro: {self.cod_livro}
                Título: {self.titulo}
                Subtitulo: {self.subtitulo}
            """,
            font=CTkFont(
                size=14,
                family="Arial"
            ),
            width=700
        )