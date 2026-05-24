# import .*
import customtkinter as ctk
import io
# from .* import .*
from customtkinter import CTkFont
from PIL import Image
# from components.*
from assets.components.livro import Livro

class AbaInicio(ctk.CTkFrame):
    def __init__(self, master, database, **kwargs):
        super().__init__(master, **kwargs)

        self.db = database

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

        self.frame_livros = ctk.CTkScrollableFrame(
            master=self,
            fg_color="transparent",
            scrollbar_button_color=("#AAAAAA", "#666666"),
            scrollbar_button_hover_color=("#999999", "#555555"),
            border_width=2,
            border_color=("#DDDDDD", "#333333")
        )
        self.frame_livros.grid(
            row=1,
            column=0,
            sticky="nsew"
        )

        self.dados_livros = self.db.buscar_todos_livros()

        self.livros = list()
        
        for cod_livro, titulo, subtitulo, capa_binario in self.dados_livros:
            capa_arquivo_virtual = io.BytesIO(capa_binario)
            capa = ctk.CTkImage(
                light_image=Image.open(capa_arquivo_virtual),
                dark_image=Image.open(capa_arquivo_virtual),
                size=(76, 100)
            )

            livro = Livro(
                master=self.frame_livros,
                cod_livro=cod_livro,
                titulo=titulo,
                subtitulo=subtitulo,
                capa=capa
            )
            self.livros.append(livro)

            capa_arquivo_virtual.close()

    def reorganizar_livros(self, eventos):
        if self.frame_livros.winfo_width() > 1:
            largura_aba_inicial = self.frame_livros.winfo_width()
        else:
            largura_aba_inicial = 650

        largura_livro = 88
        livros_por_linha = max(3, (largura_aba_inicial - 100) // largura_livro - 1)

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