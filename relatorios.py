import sqlite3
from utils import limpar_tela, confirmar

def relatorio_produtos():
    limpar_tela()
    print("\n--- RELATÓRIO DE PRODUTOS ---")

    conn = sqlite3.connect("estoque.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Produto")
    print("\n Produtos:")
    for p in cursor.fetchall():
        print(f"ID: {p[0]} | Nome: {p[1]} | Categoria: {p[2]} | Unidade: {p[3]} | Quantidade: {p[4]}")
    conn.close()
    confirmar("Relatório de produtos gerado com sucesso!")

def relatorio_fornecedores():
    limpar_tela()
    print("\n--- RELATÓRIO DE FORNECEDORES ---")

    conn = sqlite3.connect("estoque.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Fornecedor")
    print("\nFornecedores:")
    for f in cursor.fetchall():
        print(f"ID: {f[0]} | Nome: {f[1]} | Telefone: {f[2]} | Email: {f[3]}")
    conn.close()
    confirmar("Relatório de fornecedores gerado com sucesso!")

def relatorio_entradas():
    limpar_tela()
    print("\n--- RELATÓRIO DE ENTRADAS DE ESTOQUE ---")

    conn = sqlite3.connect("estoque.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT e.id_entrada, e.data, e.quantidade, p.nome, f.nome 
        FROM EntradaEstoque e
        JOIN Produto p ON p.id_produto = e.id_produto
        JOIN Fornecedor f ON f.id_fornecedor = e.id_fornecedor
    """)
    print("\nEntradas de Estoque:")
    for entrada in cursor.fetchall():
        print(f"ID: {entrada[0]} | Data: {entrada[1]} | Produto: {entrada[3]} | Quantidade: {entrada[2]} | Fornecedor: {entrada[4]}")
    conn.close()
    confirmar("Relatório de entradas de estoque gerado com sucesso!")

def relatorio_saidas():
    limpar_tela()
    print("\n--- RELATÓRIO DE SAÍDAS DE ESTOQUE ---")

    conn = sqlite3.connect("estoque.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT s.id_saida, s.data, s.quantidade, s.destino, p.nome
        FROM SaidaEstoque s
        JOIN Produto p ON p.id_produto = s.id_produto
    """)
    print("\nSaídas de Estoque:")
    for saida in cursor.fetchall():
        print(f"ID: {saida[0]} | Data: {saida[1]} | Produto: {saida[4]} | Quantidade: {saida[2]} | Destino: {saida[3]}")
    conn.close()
    confirmar("Relatório de saídas de estoque gerado com sucesso!")

def menu_relatorios():
    while True:
        limpar_tela()
        print("\n--- MENU RELATÓRIOS ---")
        print("1 - Relatório de Produtos")
        print("2 - Relatório de Fornecedores")
        print("3 - Relatório de Entradas de Estoque")
        print("4 - Relatório de Saídas de Estoque")
        print("0 - Voltar")

        op = input("Escolha uma opção: ")

        if op == "1":
            relatorio_produtos()
        elif op == "2":
            relatorio_fornecedores()
        elif op == "3":
            relatorio_entradas()
        elif op == "4":
            relatorio_saidas()
        elif op == "0":
            break
        else:
            print("Opção inválida! Tente novamente.")