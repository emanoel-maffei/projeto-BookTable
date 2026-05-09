import sqlite3
from rich import print

try:
    banco = sqlite3.connect("banco.db")
    cursor = banco.cursor()

    cursor.execute("DELETE FROM pessoas WHERE idade > 16;")

    banco.commit()
    banco.close()

    print("Os dados foram removidos com sucesso!")

except sqlite3.Error as error:
    print(f"\nErro ao excluir. \n\n\t{error}\n")