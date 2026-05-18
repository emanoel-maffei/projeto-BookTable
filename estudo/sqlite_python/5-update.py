import sqlite3
import subprocess

try:
    banco = sqlite3.connect("banco.db")
    cursor = banco.cursor()

    cursor.execute(f"UPDATE pessoas SET nome = 'felipeto' WHERE nome = 'felipe'")

    banco.commit()
    banco.close()

    print("Os dados foram atualizados com sucesso!")

except sqlite3.Error as error:
    print("\nErro. \n\n\t", error, "\n")