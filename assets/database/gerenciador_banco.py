# import .*
import sqlite3

class GerenciadorBanco:
    def __init__(self):
        self.conn = sqlite3.connect("./assets/database/sistema.db")
        self.cursor = self.conn.cursor()

        self.criar_tabela_usuarios()

    def criar_tabela_usuarios(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                cod_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT NOT NULL UNIQUE,
                senha TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def cadastrar_usuario(self, email, senha):
        self.cursor.execute("INSERT INTO usuarios (email, senha) VALUES (? , ?)", (email, senha))
        self.conn.commit()

    def buscar_usuario(self, email, senha):
        self.cursor.execute("SELECT cod_usuario FROM usuarios WHERE email = ? and senha = ?", (email, senha))
        return self.cursor.fetchone()

        