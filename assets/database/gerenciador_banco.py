# import .*
import sqlite3

class GerenciadorBanco:
    def __init__(self):
        self.conn = sqlite3.connect("./assets/database/sistema.db")
        
        self.cursor = self.conn.cursor()

        self.criar_tabela_usuarios()

    ###################
    # Tabela usuarios #
    ###################

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

    def buscar_usuario(self, email):
        self.cursor.execute("SELECT cod_usuario FROM usuarios WHERE email = ?", (email,))
        return self.cursor.fetchone()
    
    def autenticar_dados_usuario(self, email, senha):
        self.cursor.execute("SELECT cod_usuario FROM usuarios WHERE email = ? AND senha = ?", (email, senha))
        return self.cursor.fetchone() is not None
    
    #################
    # Tabela livros #
    #################
    
    def criar_tabela_livros(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS livros (
                cod_livro INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                subtitulo TEXT,
                capa BLOB NOT NULL
            )
        """)
        self.conn.commit()
    
    def cadastrar_livro(self, titulo, capa, subtitulo=""):
        self.cursor("INSERT INTO livros (titulo, subtitulo, capa) VALUES (?, ?, ?)", (titulo, subtitulo, capa))
        self.conn.commit()

    def buscar_livro(self, titulo):
        self.cursor.execute("SELECT cod_livro FROM livros WHERE titulo = ?", (titulo,))
        # Retorna uma lista de tuplas
        return self.cursor.fetchall()
        
    
    def buscar_todos_livros(self):
        self.cursor.execute("SELECT * FROM livros")
        return self.cursor.fetchall()