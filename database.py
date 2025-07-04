import sqlite3

def criar_banco():
    conn = sqlite3.connect("estoque.db")
    cursor = conn.cursor()

    # Produto
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Produto (
        id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(100) NOT NULL,
        categoria VARCHAR(100) NOT NULL,
        unidade VARCHAR(10) NOT NULL,
        quantidade_estoque INTEGER NOT NULL
    );
    """)

    # Fornecedor
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Fornecedor (
        id_fornecedor INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(100) NOT NULL,
        telefone VARCHAR(15),
        email VARCHAR(100)
    );
    """)

    # Entrada de Estoque (depois que Produto e Fornecedor já existem)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS EntradaEstoque (
        id_entrada INTEGER PRIMARY KEY AUTOINCREMENT,
        data DATE NOT NULL,
        quantidade INTEGER NOT NULL,
        id_produto INTEGER NOT NULL,
        id_fornecedor INTEGER NOT NULL,
        FOREIGN KEY (id_produto) REFERENCES Produto(id_produto),
        FOREIGN KEY (id_fornecedor) REFERENCES Fornecedor(id_fornecedor)
    );
    """)

    # Saída de Estoque (depois que Produto já existe)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS SaidaEstoque (
        id_saida INTEGER PRIMARY KEY AUTOINCREMENT,
        data DATE NOT NULL,
        quantidade INTEGER NOT NULL,
        destino VARCHAR(100) NOT NULL,
        id_produto INTEGER NOT NULL,
        FOREIGN KEY (id_produto) REFERENCES Produto(id_produto)
    );
    """)

    conn.commit()
    conn.close()
