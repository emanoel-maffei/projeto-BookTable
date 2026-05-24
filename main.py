# import .*
import customtkinter as ctk
import subprocess
# from assets.components.* import .*
from app_gui import App
# from assets.database.* import .*
from assets.database.gerenciador_banco import GerenciadorBanco

# Para limpar o terminal e facilitar a leitura das informações imprimidas ao decorrer do código
subprocess.run("cls", shell=True)

db = GerenciadorBanco()

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("./assets/themes/tema_ctk.json")

# Dependency Injection / Injeção de Dependencia
root = App(db)
root.mainloop()