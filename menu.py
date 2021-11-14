from entidades import *

def menuOpcao():
    print("-=" * 35)
    print("Esse é o menu de opções, aqui poderá escolher algumas configurações que lhe agradem!")
    while True:
        numeroInimigos = input(f"Insira o número de inimigos em jogo entre 1 e 3: ")

        if numeroInimigos not in "123": print("Opção inválida!");
        else: numeroInimigos = int(numeroInimigos);print("-=" * 35); break;


def menuAjuda():
    print("-=" * 35)
    print("Olá, seja bem vindo ao menu de ajudas!")
    print(""" --> W - CIMA\n --> D - DIREITA\n --> S - BAIXO\n --> A - ESQUERDA""")
    print(f"-> {player} é a sua posição atual.")
    print(f"-> [ ] são espaços em branco, você pode mover-se para eles.")
    print(f"-> {objective} é o objetivo, deve mover-se até atingir ele. ")
    print(f"-> {enemy} é um inimigo, evite-o à qualquer custo!")
    print("-=" * 35)
    input("Pressione ENTER para continuar: ")