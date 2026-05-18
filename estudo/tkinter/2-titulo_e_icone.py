# imports
import tkinter as tk
import subprocess

# from-imports
from tkinter import *
from tkinter import ttk

# subprocess.run("cls", shell=True)

my_app = Tk()
my_app.title("MyApp")
my_app.iconbitmap("compasso-icon.ico")

p = ttk.Label(text="Olá Mundo!")
# Usamos o método grid para organizar em linhas e a colunas a posição que seu elemento será posicionado, sendo passado como argumento a linha e a coluna.
p.grid(row=1, column=1)

my_app.mainloop()