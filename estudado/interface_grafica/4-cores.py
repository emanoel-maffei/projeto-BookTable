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
my_app.geometry("400x300")
my_app.resizable(width=False, height=False)

# Método configure() serve para alterar propriedades de um widget depois que ele já foi criado
my_app.configure(background="red")

p = ttk.Label(text="Olá Mundo!")
p.grid(row=1, column=1)

my_app.mainloop()