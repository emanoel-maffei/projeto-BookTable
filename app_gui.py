import customtkinter as ctk
from components.tela_login import TelaLogin
from customtkinter import CTkFont

# Documentação oficial do customtkinter
# https://customtkinter.tomschimansky.com/documentation/color/

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        ###########################################
        ## Configurações iniciais da janela raiz ##
        ###########################################

        # Definindo título, forma e ícone
        self.title("BookTable")
        self.geometry("600x500")
        self.minsize(width=350, height=400)
        self.maxsize(width=800, height=550)
        self.iconbitmap("./assets/icons/livro.ico")
        
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
    
        self.tela_login = TelaLogin(master=self)
        self.tela_login.pack(
            expand=True,
            fill="both"
        )
