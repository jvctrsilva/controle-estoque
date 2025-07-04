import sqlite3, os
from utils import confirmar, limpar_tela

def criar_produto():
    limpar_tela()
    print("\n--- CRIAR PRODUTO ---")
    nome = input("Nome: ")
    categoria = input("Categoria: ")
    unidade = input("Unidade: ")
    quantidade = int(input("Quantidade em estoque: "))

    conn = sqlite3.connect("estoque.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO Produto (nome, categoria, unidade, quantidade_estoque) VALUES (?, ?, ?, ?)", (nome, categoria, unidade, quantidade))
    conn.commit()
    conn.close()

    if cursor.rowcount > 0:
        confirmar("Produto criado com sucesso!")
    else:
        confirmar("Erro ao criar o produto!")


def listar_produtos():
    limpar_tela()
    print("\n--- LISTA DE PRODUTOS ---")
    conn = sqlite3.connect("estoque.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Produto")
    for linha in cursor.fetchall():
        print(f"ID: {linha[0]} | Nome: {linha[1]} | Categoria: {linha[2]} | Unidade: {linha[3]} | Quantidade em Estoque: {linha[4]}")

    conn.close()
    input("Pressione Enter para continuar...")

def atualizar_produto():
    limpar_tela()
    listar_produtos()
    print("\n--- ATUALIZAR PRODUTO ---")
    id = int(input("ID do produto a atualizar: "))
    nome = input("Novo nome: ")
    categoria = input("Nova categoria: ")
    unidade = input("Nova unidade: ")
    quantidade = int(input("Nova quantidade: "))

    conn = sqlite3.connect("estoque.db")
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE Produto
        SET nome=?, categoria=?, unidade=?, quantidade_estoque=?
        WHERE id_produto=?
    """, (nome, categoria, unidade, quantidade, id))

    conn.commit()
    conn.close()

    if cursor.rowcount > 0:
        confirmar("Produto atualizado com sucesso!")
    else:
        confirmar("Erro ao atualizar o produto!")

def excluir_produto():
    limpar_tela()
    listar_produtos()
    print("\n--- EXCLUIR PRODUTO ---")
    print("Selecione o ID do produto que deseja excluir.")
    id = int(input("ID do produto a excluir: "))

    conn = sqlite3.connect("estoque.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Produto WHERE id_produto=?", (id,))
    conn.commit()
    conn.close()

    if cursor.rowcount > 0:
        confirmar("Produto excluido com sucesso!")
    else:
        confirmar("Erro ao excluir o produto!")

def menu_produto():
    while True:
        limpar_tela()
        print("\n--- MENU PRODUTO ---")
        print("1 - Criar Produto")
        print("2 - Listar Produtos")
        print("3 - Atualizar Produto")
        print("4 - Excluir Produto")
        print("0 - Voltar")

        op = input("Escolha uma opção: ")

        if op == "1":
            criar_produto()
        elif op == "2": 
            listar_produtos()
        elif op == "3":
            atualizar_produto()
        elif op == "4":
            excluir_produto()
        elif op == "0":
            break
        else:
            print("Opção inválida!")
