# import .*
import customtkinter as ctk
# from .* import .*
from assets.components.tela_login import TelaLogin
from assets.components.tela_inicial import TelaInicial
from customtkinter import CTkFont

# Documentação oficial do customtkinter
# https://customtkinter.tomschimansky.com/documentation/color/

class App(ctk.CTk):
    def __init__(self, database):
        super().__init__()

        self.db = database

        ###########################################
        ## Configurações iniciais da janela raiz ##
        ###########################################

        # Definindo título, forma e ícone
        self.title("BookTable")
        self.geometry("600x500")
        self.minsize(width=390, height=400)
        self.maxsize(width=800, height=550)
        self.iconbitmap("./assets/icons/livros.ico")
        # self.iconbitmap("./assets/icons/livro.ico")
        
        ############
        ## Fontes ##
        ############

        self.font_family = "Arial"

        # Para textos simples
        self.font_normal= CTkFont(
            size=16,
            family=self.font_family
        )

        # Para textos simples em negrito
        self.font_bold = CTkFont(
            size=16,
            family=self.font_family,
            weight="bold"
        )

        # Para textos grandes
        self.font_medium = CTkFont(
            size=24,
            family=self.font_family
        )

        #############################################
        ## Criando a interface por meio de classes ##
        #############################################
    
        self.tela_login = TelaLogin(
            master=self,
            database=self.db,
            action=self.ir_tela_inicial,
            fg_color="transparent"
        )
        self.tela_login.pack(
            expand=True,
            fill="both",
        )

        self.tela_inicial = TelaInicial(
            master=self,
            database=self.db,
            fg_color="transparent"
        )
        self.tela_inicial.pack_forget()

    def ir_tela_inicial(self):
        self.tela_login.pack_forget()
        self.tela_inicial.pack(
            expand=True,
            fill="both"
        )

    def ir_tela_login(self):
        self.tela_inicial.pack_forget()
        self.tela_login.pack(
            expand=True,
            fill="both"
        )