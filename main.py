# Biblioteca sqlite3
# -------------------
# A biblioteca `sqlite3` é uma biblioteca nativa do Python que permite a interação
# com bancos de dados SQLite, que são bancos de dados relacionais leves e armazenados
# em um único arquivo no disco. Essa biblioteca fornece uma interface para executar
# comandos SQL como criação de tabelas, inserção, atualização, exclusão e consulta
# de dados, facilitando o desenvolvimento de aplicações que precisam de persistência
# de dados sem a necessidade de configurar um servidor de banco de dados.

from database import criar_banco
import produto, fornecedor, estoque, relatorios

criar_banco()

def main():
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1 - Gerenciar Produtos")
        print("2 - Gerenciar Fornecedores")
        print("3 - Gerenciar Estoque")
        print("4 - Relatórios")
        print("0 - Sair")

        op = input("Escolha uma opção: ")

        if op == "1":
            produto.menu_produto()
        elif op == "2":
            fornecedor.menu_fornecedor()
        elif op == "3":
            estoque.menu_estoque()
        elif op == "4":
            relatorios.menu_relatorios()
        elif op == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()