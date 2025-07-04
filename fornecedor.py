import sqlite3, os
from utils import confirmar, limpar_tela

def criar_fornecedor():
    limpar_tela()
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")

    conn = sqlite3.connect("estoque.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO Fornecedor (nome, telefone, email) VALUES (?, ?, ?)", (nome, telefone, email))
    conn.commit()
    conn.close()

    if cursor.rowcount > 0:
        confirmar("Fornecedor criado com sucesso!")
    else:
        confirmar("Erro ao criar o fornecedor!")

def listar_fornecedores():
    limpar_tela()
    conn = sqlite3.connect("estoque.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Fornecedor")
    for linha in cursor.fetchall():
        print(f"ID: {linha[0]} | Nome: {linha[1]} | Telefone: {linha[2]} | Email: {linha[3]}")

    conn.close()
    input("Pressione Enter para continuar...")

def atualizar_fornecedor():
    limpar_tela()
    listar_fornecedores()
    id = int(input("ID do fornecedor: "))
    nome = input("Novo nome: ")
    telefone = input("Novo telefone: ")
    email = input("Novo email: ")

    conn = sqlite3.connect("estoque.db")
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE Fornecedor
        SET nome=?, telefone=?, email=?
        WHERE id_fornecedor=?
    """, (nome, telefone, email, id))

    conn.commit()
    conn.close()

    if cursor.rowcount > 0:
        confirmar("Fornecedor atualizado com sucesso!")
    else:
        confirmar("Erro ao atualizar o fornecedor!")

def excluir_fornecedor():
    limpar_tela()
    listar_fornecedores()
    id = int(input("ID do fornecedor a excluir: "))

    conn = sqlite3.connect("estoque.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Fornecedor WHERE id_fornecedor=?", (id,))
    conn.commit()
    conn.close()

    if cursor.rowcount > 0:
        confirmar("Fornecedor excluído com sucesso!")
    else:
        confirmar("Erro ao excluir o fornecedor!")

def menu_fornecedor():
    while True:
        limpar_tela()
        print("\n--- MENU FORNECEDOR ---")
        print("1 - Criar Fornecedor")
        print("2 - Listar Fornecedores")
        print("3 - Atualizar Fornecedor")
        print("4 - Excluir Fornecedor")
        print("0 - Voltar")

        op = input("Escolha uma opção: ")

        if op == "1":
            criar_fornecedor()
        elif op == "2":
            listar_fornecedores()
        elif op == "3":
            atualizar_fornecedor()
        elif op == "4":
            excluir_fornecedor()
        elif op == "0":
            break
        else:
            print("Opção inválida!")        