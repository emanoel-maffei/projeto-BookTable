# import .*
import customtkinter as ctk
# from .* import .*
from components.aba_inicio import AbaInicio
from components.aba_curtidos import AbaCurtidos
from components.aba_baixados import AbaBaixados

class PartePrincipal(ctk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        #########################
        ## Construção das abas ##
        #########################

        self.add("Inicio")
        self.add("Curtidos")
        self.add("Baixados")

        ## Aba Inicio ##

        self.frame_aba_inicio = AbaInicio(
            master=self.tab("Inicio"),
            fg_color="#F0F0F0"
        )
        self.frame_aba_inicio.pack(
            expand=True,
            fill="both"
        )
        
        ## Aba Curtidos ##
        self.frame_aba_curtidos = AbaCurtidos(
            master=self.tab("Curtidos"),
            fg_color="#F0F0F0"
        )
        self.frame_aba_curtidos.pack(
            expand=True,
            fill="both"
        )
        
        ## Aba Baixados ##
        self.frame_aba_baixados = AbaBaixados(
            master=self.tab("Baixados"),
            fg_color="#F0F0F0"
        )
        self.frame_aba_baixados.pack(
            expand=True,
            fill="both"
        )
