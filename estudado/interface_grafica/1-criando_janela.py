# imports
import tkinter as tk
import subprocess

# from-imports
from tkinter import *
from tkinter import ttk

subprocess.run("cls", shell=True)

my_app = Tk()

p = ttk.Label(text="Olá Mundo!").place(x=1, y=10)

my_app.mainloop()