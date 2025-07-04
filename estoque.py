import sqlite3, os
from utils import confirmar, limpar_tela

from datetime import datetime

def entrada_estoque():

    conn = sqlite3.connect("estoque.db")
    cursor = conn.cursor()

    limpar_tela()
    print("\n--- LISTA DE PRODUTOS ---")
    
    cursor.execute("SELECT * FROM Produto")
    for linha in cursor.fetchall():
        print(f"ID: {linha[0]} | Nome: {linha[1]} | Categoria: {linha[2]} | Unidade: {linha[3]} | Quantidade em Estoque: {linha[4]}")

    print("\n--- LISTA DE FORNECEDORES ---")
    cursor.execute("SELECT * FROM Fornecedor")
    for linha in cursor.fetchall():
        print(f"ID: {linha[0]} | Nome: {linha[1]} | Telefone: {linha[2]} | Email: {linha[3]}")

    print("\n--- ENTRADA DE ESTOQUE ---")
    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    quantidade = int(input("Quantidade: "))
    id_produto = int(input("ID do Produto: "))
    id_fornecedor = int(input("ID do Fornecedor: "))

    cursor.execute("INSERT INTO EntradaEstoque (data, quantidade, id_produto, id_fornecedor) VALUES (?, ?, ?, ?)", (data, quantidade, id_produto, id_fornecedor))
    
    cursor.execute("""
            UPDATE Produto
            SET quantidade_estoque = quantidade_estoque + ?
            WHERE id_produto = ?
        """, (quantidade, id_produto))

    conn.commit()
    conn.close()

    if cursor.rowcount > 0:
        confirmar("Entrada realizada com sucesso!")
    else:
        confirmar("Erro ao realizar a entrada!")

def saida_estoque():
    conn = sqlite3.connect("estoque.db")
    cursor = conn.cursor()

    limpar_tela()
    print("\n--- LISTA DE PRODUTOS ---")
    cursor.execute("SELECT * FROM Produto")
    for linha in cursor.fetchall():
        print(f"ID: {linha[0]} | Nome: {linha[1]} | Categoria: {linha[2]} | Unidade: {linha[3]} | Quantidade em Estoque: {linha[4]}")

    print("\n--- SAÍDA DE ESTOQUE ---")
    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    quantidade = int(input("Quantidade: "))
    destino = input("Destino: ")
    id_produto = int(input("ID do Produto: "))

    cursor.execute("INSERT INTO SaidaEstoque (data, quantidade, destino, id_produto) VALUES (?, ?, ?, ?)", (data, quantidade, destino, id_produto))

    # Verifica se a quantidade em estoque é suficiente
    cursor.execute("SELECT quantidade_estoque FROM Produto WHERE id_produto = ?", (id_produto,))
    estoque_atual = cursor.fetchone()

    # Se houver estoque e a quantidade for suficiente, atualiza o estoque
    if estoque_atual and estoque_atual[0] >= quantidade:
        cursor.execute("""
            UPDATE Produto
            SET quantidade_estoque = quantidade_estoque - ?
            WHERE id_produto = ?
        """, (quantidade, id_produto))
    else:
        confirmar("Quantidade insuficiente em estoque!")
        conn.close()
        return
    conn.commit()
    conn.close()

    if cursor.rowcount > 0:
        confirmar("Saída realizada com sucesso!")
    else:
        confirmar("Erro ao realizar a saída!")

def menu_estoque():
    while True:
        limpar_tela()
        print("\n--- MENU ESTOQUE ---")
        print("1 - Entrada de Estoque")
        print("2 - Saída de Estoque")
        print("0 - Voltar")

        op = input("Escolha uma opção: ")

        if op == "1":
            entrada_estoque()
        elif op == "2":
            saida_estoque()
        elif op == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")