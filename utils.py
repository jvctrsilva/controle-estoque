import os

def confirmar(mensagem):
    print(f"\n {mensagem}")
    input("Pressione Enter para continuar...")
    
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
