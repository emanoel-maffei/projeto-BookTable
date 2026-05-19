# import .*
import customtkinter as ctk
# from .* import .*
from customtkinter import CTkFont
from PIL import Image # Python Imaging Library

class TelaInicial(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        ##################################
        ## Configurações da TelaInicial ##
        ##################################

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        ##############################
        ## Construção dos elementos ##
        ##############################

        ## Linha 0 | Coluna 0 ##

        self.frame_barra_lateral = ctk.CTkFrame(
            master=self,
            corner_radius=0,
            fg_color=("#FFFFFF", "#000000"),
        )
        self.frame_barra_lateral.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        # Botão Tela Inicial
        self.image_casa = ctk.CTkImage(
            light_image=Image.open("./assets/imgs/casa_modo_claro.png"),
            dark_image=Image.open("./assets/imgs/casa_modo_escuro.png"),
            size=(20, 20)
        )
        self.button_inicial = ctk.CTkButton(
            master=self.frame_barra_lateral,
            image=self.image_casa,
            text="",
            fg_color="transparent",
            hover_color=("#DDDDDD", "#333333"),
            width=30,
            height=30,
            border_width=2,
            border_color=("#DDDDDD", "#333333")
        )
        self.button_inicial.pack(
            padx=(10, 10),
            pady=(10, 0)
        )

        # botão Tela Curtidos
        self.image_coracao = ctk.CTkImage(
            light_image=Image.open("./assets/imgs/coracao_modo_claro.png"),
            dark_image=Image.open("./assets/imgs/coracao_modo_escuro.png"),
            size=(20, 20)
        )
        self.button_curtidos = ctk.CTkButton(
            master=self.frame_barra_lateral,
            image=self.image_coracao,
            text="",
            fg_color="transparent",
            hover_color=("#DDDDDD", "#333333"),
            width=30,
            height=30,
            border_width=2,
            border_color=("#DDDDDD", "#333333")
        )
        self.button_curtidos.pack(
            padx=(10, 10),
            pady=(10, 0)
        )

        self.image_download = ctk.CTkImage(
            light_image=Image.open("./assets/imgs/download_modo_claro.png"),
            dark_image=Image.open("./assets/imgs/download_modo_escuro.png"),
            size=(20, 20)
        )
        self.button_baixados =  ctk.CTkButton(
            master=self.frame_barra_lateral,
            image=self.image_download,
            text="",
            fg_color="transparent",
            hover_color=("#DDDDDD", "#333333"),
            width=30,
            height=30,
            border_width=2,
            border_color=("#DDDDDD", "#333333")
        )
        self.button_baixados.pack(
            padx=(10, 10),
            pady=(10, 0)
        )

        
        self.image_tema = ctk.CTkImage(
            light_image=Image.open("./assets/imgs/sol.png"),
            dark_image=Image.open("./assets/imgs/lua.png"),
        )
        self.button_tema = ctk.CTkButton(
            master=self.frame_barra_lateral,
            text="",
            image=self.image_tema,
            fg_color="transparent",
            hover_color=("#EEEE00", "#FFFFFF"),
            width=30,
            height=30,
            border_width=2,
            border_color=("#FFFF00", "#000088"),
            command=self.alternar_tema
        )
        self.button_tema.pack(
            padx=(10, 10),
            pady=(10, 10),
            side="bottom"
        )

        ## Linha 0 | Coluna 1 ##

        self.frame_parte_principal = ctk.CTkFrame(
            master=self,
            corner_radius=0,
            fg_color=("#FFFFFF", "#000000")
        )
        self.frame_parte_principal.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=(10, 0)
        )

    def alternar_tema(self):
        if ctk.get_appearance_mode() == "Light":
            ctk.set_appearance_mode("Dark")
        else:
            ctk.set_appearance_mode("Light")