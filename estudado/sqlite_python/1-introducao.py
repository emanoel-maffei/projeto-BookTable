import sqlite3
from rich import print

banco = sqlite3.connect("banco.db")
cursor = banco.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS pessoas (
    nome TEXT,
    idade INTGER,
    email TEXT
);""")

cursor.execute("INSERT INTO pessoas VALUES ('leonardo', 17, 'leonardo@email.com');")
cursor.execute("INSERT INTO pessoas VALUES ('felipe', 17, 'felipe@email.com');")

banco.commit()

cursor.execute("SELECT * FROM pessoas;")
pessoas = cursor.fetchall()

print(pessoas)