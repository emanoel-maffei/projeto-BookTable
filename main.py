import sqlite3, subprocess
import tkinter as tk
from rich import print

subprocess.run("clear")

try:
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contas (
        id INTEGER PRIMARY KEY,
        email TEXT NOT NULL UNIQUE,
        senha TEXT NOT NULL
    );
    """)

    def autenticar_login():
        email = email_entry.get()
        senha = senha_entry.get()

        cursor.execute("SELECT email, senha FROM contas;")
        response = cursor.fetchall()

        if (email, senha) in response:
            status_label["text"] = "Login feito com sucesso."
            status_label["foreground"] = "green"
        else:
            status_label["text"] = "Os dados são inválidos."
            status_label["foreground"] = "red"

    app = tk.Tk()
    app.title("BookTable")
    # app.iconbitmap("compasso.ico")
    app.geometry("400x300")

    tk.Label(app, text="BookTable", pady=20).pack()

    tk.Label(app, text="Email:",).pack()
    email_entry = tk.Entry(app)
    email_entry.pack()

    tk.Label(app, text="Senha:",).pack()
    senha_entry = tk.Entry(app)
    senha_entry.pack()

    tk.Button(app, text="Login", command=autenticar_login).pack()
    status_label = tk.Label(app, text="")
    status_label.pack()

    app.mainloop()

    conn.commit()
    conn.close()

except sqlite3.Error as error:
    print(f"\nErro:\n\n\t{error}\n")