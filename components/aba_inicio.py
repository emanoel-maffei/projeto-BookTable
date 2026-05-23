# import .*
import customtkinter as ctk
import subprocess
# from .* import .*
from customtkinter import CTkFont
from PIL import Image
# from components.*
from components.livro import Livro

class AbaInicio(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        ##########################
        ## Configurações da Aba ##
        ##########################

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        
        ##############################
        ## Construção dos elementos ##
        ##############################

        ## Linha 0 | Coluna 0 ##

        self.frame_consulta = ctk.CTkFrame(
            master=self,
            fg_color="transparent",
            height=50
        )
        self.frame_consulta.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        self.entry_consulta = ctk.CTkEntry(
            master=self.frame_consulta,
            placeholder_text="Consulte aqui.",
            width=300,
            height=30,
            border_color=("#DDDDDD", "#333333"),
            font=CTkFont(
                size=14,
                family="Arial"
            )
        )
        self.entry_consulta.place(
            relx=0.5,
            rely=0.5,
            anchor="center",
            relw=0.9
        )

        ## Linha 1 | Coluna 0 ##
        #
        # Criação dos elementos correspondentes a livros

        self.frame_livros = ctk.CTkFrame(
            master=self,
            fg_color="transparent"
        )
        self.frame_livros.grid(
            row=1,
            column=0,
            sticky="nsew"
        )

        # Elementos representando Livros

        self.livros = list()
        self.image_livro = ctk.CTkImage(
            light_image=Image.open("./assets/icons/livro.ico"),
            dark_image=Image.open("./assets/icons/livro.ico"),
            size=(76, 100)
        )

        for i in range(18):
            self.livros.append(Livro(
                master=self.frame_livros,
                image=self.image_livro
            ))

        self.bind("<Configure>", self.reorganizar_livros)

    def reorganizar_livros(self, evento):
        print(self.frame_livros.winfo_width())

        largura_aba_inicial = self.frame_livros.winfo_width()
        largura_livro = 88
        livros_por_linha = max(1, (largura_aba_inicial // largura_livro))

        linha = 0
        coluna = 0

        for livro in self.livros:
            if coluna >= livros_por_linha:
                linha += 1
                coluna = 0

            livro.grid(
                row=linha,
                column=coluna
            )
            coluna += 1