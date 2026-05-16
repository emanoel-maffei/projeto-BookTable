# from .* import .*
from customtkinter import CTkFont
from rich import print
# import .*
import sqlite3, subprocess
import customtkinter as ctk

subprocess.run("cls", shell=True)
ctk.set_appearance_mode("Light")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        ###########################################
        ## Configurações iniciais da janela raiz ##
        ###########################################

        self.title("BookTable")
        self.geometry("600x500")
        self.minsize(width=300, height=400)
        self.iconbitmap("./livro.ico")
        # self.resizable(True, True) # Já por padrão
        # self.state("zoomed")

        
        ############
        ## Fontes ##
        ############

        # Para Label simples
        self.label_font = CTkFont(
            size=16,
            family="Arial"
        )

        # Para Label em negrito
        self.label_font_bold = CTkFont(
            size=16,
            family="Arial",
            weight="bold"
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
    def __init__(self, master):
        super().__init__(master)

        # Configurações da Grade (Grid)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((1, 2), weight=1)

        # Switch -> Alternador do Modo Escuro
        self.switch_modo_escuro = ctk.CTkSwitch(
            master=self,
            text="Modo Escuro",
            command=self.alternar_modo_escuro
        )
        self.switch_modo_escuro.place(
            x=10, 
            y=10,
        )

        # Label -> Título Principal
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

        # Frame -> Container Campo Usuário
        self.frame_usuario = ctk.CTkFrame(
            master=self,
            fg_color="transparent"
        )
        self.frame_usuario.grid(row=1, column=0, sticky="nsew")

        # frame_usuario > Frame -> Centralizador do Rótulo e Campo
        self.frame_usuario_centralizador = ctk.CTkFrame(
            master=self.frame_usuario,
            fg_color="transparent",
        )
        self.frame_usuario_centralizador.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        # frame_usuario > Label -> Rótulo para o Campo do Usuário
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

        # frame_usuario > Entry:
        self.entry_usuario = ctk.CTkEntry(
            master=self.frame_usuario_centralizador,
            placeholder_text="Digite seu email.",
            width=300
        )
        self.entry_usuario.pack(padx=(16, 16))

        # Frame -> Container Campo Senha
        self.frame_senha = ctk.CTkFrame(
            master=self,
            fg_color="transparent"
        )
        self.frame_senha.grid(row=2, column=0, sticky="nsew")

        # frame_senha > Frame -> Centralizador do Rótulo e Campo da Senha
        self.frame_senha_centralizador = ctk.CTkFrame(
            master=self.frame_senha,
            fg_color="transparent"
        )
        self.frame_senha_centralizador.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        # frame_senha > Label -> Rótulo do Campo da Senha
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

        # frame_senha > Entry -> Campo da Senha
        self.entry_senha = ctk.CTkEntry(
            master=self.frame_senha_centralizador,
            placeholder_text="Digite a senha.",
            width=300
        )
        self.entry_senha.pack(padx=(16, 16))

    def alternar_modo_escuro(self):
        ctk.set_appearance_mode("Dark" if self.switch_modo_escuro.get() else "Light")

root = App()
root.mainloop()