# from .* import .*
from customtkinter import CTkFont
from rich import print
# import .*
import sqlite3, subprocess
import customtkinter as ctk

# Documentação oficial do customtkinter
# https://customtkinter.tomschimansky.com/documentation/color/

subprocess.run("cls", shell=True)
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        ###########################################
        ## Configurações iniciais da janela raiz ##
        ###########################################

        # Definindo título, forma e ícone
        self.title("BookTable")
        self.geometry("600x500")
        self.minsize(width=300, height=400)
        self.iconbitmap("./livro.ico")

        
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

class TelaLogin(ctk.CTkFrame):
    '''Cria um frame contendo todos os elementos de uma tela de login pronta'''
    def __init__(self, master):
        '''
        Cria e adiciona todos os elementos ao frame
        
        Parametros:
            - self: Recebe o próprio objeto que disparou o método
            - master: Recebe o elemento ao qual o atual será implementado
        '''
        
        # Para de fato criar um frame
        super().__init__(master)
        
        ############################
        ## Configurações do Frame ##
        ############################
    
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((1, 2, 3), weight=1)

        ##############################
        ## Construção dos elementos ##
        ##############################
        
        ## Elementos de posicionamento absoluto ##
        # 
        # Para não atrapalhar o posicionamento de outros elementos

        self.switch_modo_escuro = ctk.CTkSwitch(
            master=self,
            text="Modo Escuro",
            command=self.alternar_modo_escuro
        )
        self.switch_modo_escuro.place(
            x=10, 
            y=10,
        )
        
        ## Linha 0 ##

        self.label_titulo = ctk.CTkLabel(
            master=self,
            text="BookTable",
            text_color="white",
            fg_color="blue",
            corner_radius=16,
            font=CTkFont(
                size=44,
                family="Arial"
            )
        )
        self.label_titulo.grid(
            row=0, 
            column=0,
            ipadx=16, 
            ipady=16, 
            pady=(60, 0)
        )

        ## Linha 1 ##

        # Este Frame foi criado para ocupar a linha 1 inteira
        self.frame_usuario = ctk.CTkFrame(
            master=self,
            fg_color="transparent"
        )
        self.frame_usuario.grid(row=1, column=0, sticky="nsew")

        # Este frame foi criado para centralizar os elementos dentro do Frame que ocupa a linha 1
        self.frame_usuario_centralizador = ctk.CTkFrame(
            master=self.frame_usuario,
            fg_color="transparent",
        )
        self.frame_usuario_centralizador.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        self.label_usuario = ctk.CTkLabel(
            master=self.frame_usuario_centralizador,
            text="Usuário:",
            font=CTkFont(
                size=16,
                family="Arial",
                weight="bold"
            )
        )
        self.label_usuario.pack(pady=(0, 20))

        self.entry_usuario = ctk.CTkEntry(
            master=self.frame_usuario_centralizador,
            placeholder_text="Digite seu email.",
            width=300
        )
        self.entry_usuario.pack(padx=(16, 16))

        ## Linha 2 ##

        # Este Frame foi criado para ocupar a linha 2 inteira
        self.frame_senha = ctk.CTkFrame(
            master=self,
            fg_color="transparent"
        )
        self.frame_senha.grid(row=2, column=0, sticky="nsew")

        # Este frame foi criado para centralizar os elementos dentro do Frame que ocupa a linha 2 
        self.frame_senha_centralizador = ctk.CTkFrame(
            master=self.frame_senha,
            fg_color="transparent"
        )
        self.frame_senha_centralizador.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        self.label_senha = ctk.CTkLabel(
            master=self.frame_senha_centralizador,
            text="Senha:",
            font=CTkFont(
                size=16,
                family="Arial",
                weight="bold"
            )
        )
        self.label_senha.pack(pady=(0, 20))

        self.entry_senha = ctk.CTkEntry(
            master=self.frame_senha_centralizador,
            placeholder_text="Digite a senha.",
            width=300
        )
        self.entry_senha.pack(padx=(16, 16))

        ## Linha 3 ##

        self.frame_entrar = ctk.CTkFrame(
            master=self,
            fg_color="transparent"
        )
        self.frame_entrar.grid(
            row=3,
            column=0,
            sticky="nsew"
        )

        self.button_entrar = ctk.CTkButton(
            master=self.frame_entrar,
            text="Entrar",
            command=self.entrar,
            width=100,
            height=50,
            font=CTkFont(
                size=24,
                family="Arial"
            )
        )
        self.button_entrar.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

    def alternar_modo_escuro(self):
        '''Alterna o tema das janelas entre claro e escuro com base no estado do elemento Switch da janela raiz'''

        ctk.set_appearance_mode("Dark" if self.switch_modo_escuro.get() else "Light")

    def entrar(self):
        print("[Entrar] Clicked.")
        pass

root = App()
root.mainloop()