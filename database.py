import sqlite3

def criar_banco():
    conn = sqlite3.connect("estoque.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Produto (
        id_produto INTEGER PRIMARY KEY,
        nome TEXT,
        categoria TEXT,
        unidade TEXT,
        quantidade_estoque INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Fornecedor (
        id_fornecedor INTEGER PRIMARY KEY,
        nome TEXT,
        telefone TEXT,
        email TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS EntradaEstoque (
        id_entrada INTEGER PRIMARY KEY,
        data TEXT,
        quantidade INTEGER,
        id_produto INTEGER,
        id_fornecedor INTEGER,
        FOREIGN KEY(id_produto) REFERENCES Produto(id_produto),
        FOREIGN KEY(id_fornecedor) REFERENCES Fornecedor(id_fornecedor)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS SaidaEstoque (
        id_saida INTEGER PRIMARY KEY,
        data TEXT,
        quantidade INTEGER,
        destino TEXT,
        id_produto INTEGER,
        FOREIGN KEY(id_produto) REFERENCES Produto(id_produto)
    )
    """)

    conn.commit()
    conn.close()
