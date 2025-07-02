from database import criar_banco
import produto

criar_banco()

def menu():
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1 - Criar Produto")
        print("2 - Listar Produtos")
        print("3 - Atualizar Produto")
        print("4 - Excluir Produto")
        print("0 - Sair")

        op = input("Escolha uma opção: ")

        if op == "1":
            produto.criar_produto()
        elif op == "2":
            produto.listar_produtos()
        elif op == "3":
            produto.atualizar_produto()
        elif op == "4":
            produto.excluir_produto()
        elif op == "0":
            break
        else:
            print("Opção inválida!")

menu()
