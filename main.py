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

        self.title("BookTable")
        self.geometry("600x500")
        self.minsize(width=300, height=400)
        self.iconbitmap("./livro.ico")
        # self.resizable(True, True) # Já por padrão
        # self.state("zoomed")

        ## Fontes ##

        # Fonte para Label em negrito
        self.label_font = CTkFont(
            size=16,
            family="Arial"
        )

        # Fonte para Label simples
        self.label_font_bold = CTkFont(
            size=16,
            family="Arial",
            weight="bold"
        )

        # Configurações da Grade (Grid)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((1, 2), weight=1)

        # Chamada das funções construtoras da interface 
        self.criar_tela_login()

    def criar_tela_login(self):
        # Switch -> Alternador do Modo Escuro
        switch_modo_escuro = ctk.CTkSwitch(
            master=self,
            text="Modo Escuro"
        )
        switch_modo_escuro.place(
            x=10, 
            y=10,
        )

        # Label -> Título Principal
        ctk.CTkLabel(
            master=self,
            text="BookTable",
            text_color="white",
            fg_color="blue",
            corner_radius=16,
            font=CTkFont(
                size=44,
                family="Arial"
            )
        ).grid(
            row=0, 
            column=0,
            ipadx=16, 
            ipady=16, 
            pady=(60, 0)
        )

        # Frame -> Container Campo Usuário
        frame_usuario = ctk.CTkFrame(
            master=self,
            fg_color="transparent"
        )
        frame_usuario.grid(row=1, column=0, sticky="nsew")

        # frame_usuario > Frame -> Centralizador do Rótulo e Campo
        frame_usuario_centralizador = ctk.CTkFrame(
            master=frame_usuario,
            fg_color="transparent",
        )
        frame_usuario_centralizador.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        # frame_usuario > Label -> Rótulo para o Campo do Usuário
        ctk.CTkLabel(
            master=frame_usuario_centralizador,
            text="Usuário:",
            font=CTkFont(
                size=16,
                family="Arial",
                weight="bold"
            )
        ).pack(pady=(0, 20))

        # frame_usuario > Entry:
        entry_usuario = ctk.CTkEntry(
            master=frame_usuario_centralizador,
            placeholder_text="Digite seu email.",
            width=300
        )
        entry_usuario.pack(padx=(16, 16))

        # Frame -> Container Campo Senha
        frame_senha = ctk.CTkFrame(
            master=self,
            fg_color="transparent"
        )
        frame_senha.grid(row=2, column=0, sticky="nsew")

        # frame_senha > Frame -> Centralizador do Rótulo e Campo da Senha
        frame_senha_centralizador = ctk.CTkFrame(
            master=frame_senha,
            fg_color="transparent"
        )
        frame_senha_centralizador.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        # frame_senha > Label -> Rótulo do Campo da Senha
        ctk.CTkLabel(
            master=frame_senha_centralizador,
            text="Senha:",
            font=CTkFont(
                size=16,
                family="Arial",
                weight="bold"
            )
        ).pack(pady=(0, 20))

        # frame_senha > Entry -> Campo da Senha
        entry_senha = ctk.CTkEntry(
            master=frame_senha_centralizador,
            placeholder_text="Digite a senha.",
            width=300
        )
        entry_senha.pack(padx=(16, 16))

root = App()
root.mainloop()