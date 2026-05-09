import sqlite3
import subprocess

nome = input("Digite seu nome: ")

idade = 0
while True:
    try:
        idade = int(input("Digite sua idade: "))
    except ValueError:
        input("\nDigite um valor válido. (Enter) ")
        subprocess.run("cls", shell=True)
    else:
        break

email = input("Digite seu email: ")

try:
    banco = sqlite3.connect("banco.db")
    cursor = banco.cursor()

    cursor.execute(f"INSERT INTO pessoas VALUES ('{nome}', {idade}, '{email}');")

    banco.commit()
    banco.close()

    print("Os dados foram inseridos com sucesso!")

except sqlite3.Error as error:
    print("\nErro. \n\n\t", error, "\n")