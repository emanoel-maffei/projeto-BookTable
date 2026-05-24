# import .*
import customtkinter as ctk
# from .* import .*
from customtkinter import CTkFont
from assets.components.barra_lateral import BarraLateral
from assets.components.parte_principal import PartePrincipal

class TelaInicial(ctk.CTkFrame):
    def __init__(self, master, database, funcao_mudar_tela, **kwargs):
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
            funcao_mudar_tela=funcao_mudar_tela,
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
        
        self.bind("<Configure>", self.janela_redimencionada)

    def alternar_tema(self):
        if ctk.get_appearance_mode() == "Light":
            ctk.set_appearance_mode("Dark")
        else:
            ctk.set_appearance_mode("Light")

    def definir_aba_tabview(self, aba):
        self.tabview_parte_principal.set(aba)

    def janela_redimencionada(self, eventos):
        self.tabview_parte_principal.reorganizar_livros(eventos)