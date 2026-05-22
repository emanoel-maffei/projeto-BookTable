# import .*
import customtkinter as ctk
import sqlite3
import subprocess
# from .* import .*
from app_gui import App

# Para limpar o terminal e facilitar a leitura das informações imprimidas ao decorrer do código
subprocess.run("cls", shell=True)

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("./assets/themes/tema_ctk.json")
     
root = App()
root.mainloop()