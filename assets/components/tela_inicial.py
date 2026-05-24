# import .*
import customtkinter as ctk
# from .* import .*
from customtkinter import CTkFont
from assets.components.barra_lateral import BarraLateral
from assets.components.parte_principal import PartePrincipal

class TelaInicial(ctk.CTkFrame):
    def __init__(self, master, database, **kwargs):
        super().__init__(master, **kwargs)

        self.db = database

        ##################################
        ## Configurações da TelaInicial ##
        ##################################

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        ##############################
        ## Construção dos elementos ##
        ##############################

        ## Linha 0 | Coluna 0 ##

        self.frame_barra_lateral = BarraLateral(
            master=self,
            database=self.db,
            corner_radius=0,
            fg_color=("#FFFFFF", "#000000"),
        )
        self.frame_barra_lateral.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        ## Linha 0 | Coluna 1 ##

        self.tabview_parte_principal = PartePrincipal(
            master=self,
            database=self.db,
            fg_color=("#FFFFFF", "#000000")
        )
        self.tabview_parte_principal.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=(5, 5),
            pady=(0, 5)
        )

        self.bind("<Configure>", self.reorganizar_livros)

    def alternar_tema(self):
        if ctk.get_appearance_mode() == "Light":
            ctk.set_appearance_mode("Dark")
        else:
            ctk.set_appearance_mode("Light")

    def reorganizar_livros(self, eventos):
        self.tabview_parte_principal.frame_aba_inicio.reorganizar_livros(eventos)
        # self.tabview_parte_principal.frame_aba_curtidos.reorganizar_livros(eventos)
        # self.tabview_parte_principal.frame_aba_baixados.reorganizar_livros(eventos)