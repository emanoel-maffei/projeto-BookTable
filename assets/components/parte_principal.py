# import .*
import customtkinter as ctk
# from .* import .*
from assets.components.aba_inicio import AbaInicio
from assets.components.aba_curtidos import AbaCurtidos
from assets.components.aba_baixados import AbaBaixados

class PartePrincipal(ctk.CTkTabview):
    def __init__(self, master, database, **kwargs):
        super().__init__(master, **kwargs)

        self.db = database

        #########################
        ## Construção das abas ##
        #########################

        self.add("Inicio")
        self.add("Curtidos")
        self.add("Baixados")

        ## Aba Inicio ##

        self.frame_aba_inicio = AbaInicio(
            master=self.tab("Inicio"),
            database=self.db,
            fg_color="transparent"
        )
        self.frame_aba_inicio.pack(
            expand=True,
            fill="both"
        )
        
        ## Aba Curtidos ##
        self.frame_aba_curtidos = AbaCurtidos(
            master=self.tab("Curtidos"),
            database=self.db,
            fg_color="transparent"
        )
        self.frame_aba_curtidos.pack(
            expand=True,
            fill="both"
        )
        
        ## Aba Baixados ##
        self.frame_aba_baixados = AbaBaixados(
            master=self.tab("Baixados"),
            database=self.db,
            fg_color="transparent"
        )
        self.frame_aba_baixados.pack(
            expand=True,
            fill="both"
        )
