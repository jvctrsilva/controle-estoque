import sqlite3

def criar_produto():
    id = int(input("ID: "))
    nome = input("Nome: ")
    categoria = input("Categoria: ")
    unidade = input("Unidade: ")
    quantidade = int(input("Quantidade em estoque: "))

    conn = sqlite3.connect("estoque.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO Produto VALUES (?, ?, ?, ?, ?)", (id, nome, categoria, unidade, quantidade))
    conn.commit()
    conn.close()

def listar_produtos():
    conn = sqlite3.connect("estoque.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Produto")
    for linha in cursor.fetchall():
        print(linha)

    conn.close()

def atualizar_produto():
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

def excluir_produto():
    id = int(input("ID do produto a excluir: "))

    conn = sqlite3.connect("estoque.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Produto WHERE id_produto=?", (id,))
    conn.commit()
    conn.close()
