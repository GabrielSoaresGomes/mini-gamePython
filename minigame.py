import random


# Definindo funções
def menuOpcao():
    print("Esse é o menu de opções, aqui poderá escolher algumas configurações que lhe agradem!")
    while True:
        numeroInimigos = input("Insira o número de inimigos em jogo entre 1 à 3: ")
        try int(numeroInimigos
        except


def menuAjuda():
    print("Olá, seja bem vindo ao menu de ajudas!")
    print(""" --> W - CIMA\n --> D - DIREITA\n --> S - BAIXO\n --> A - ESQUERDA""")
    print(f"-> {player} é a sua posição atual.")
    print(f"-> [ ] são espaços em branco, você pode mover-se para eles.")
    print(f"-> {objective} é o objetivo, deve mover-se até atingir ele. ")
    print(f"-> {enemy} é um inimigo, evite-o à qualquer custo!")
    input("Pressione ENTER para continuar: ")

def verificarMovimento(nova_posicao):
    if (nova_posicao < 0) or (nova_posicao > 49) or \
            ((playerPosition in (9, 19, 29, 39, "\n")) and move == "D") or \
            ((playerPosition in (0, 10, 20, 30, 40, "\n")) and move == "A"):
        return True


def retornar():
    for c in range(len(line0)):
        if line0[c] == player:
            line0[c] = playerPosition


def move_up(position):
    position -= 10
    return position


def move_right(position):
    position += 1
    return position


def move_down(position):
    position += 10
    return position


def move_left(position):
    position -= 1
    return position


# Definindo variaveis
player = "\033[1;32mO\033[m"
playerPosition = 0
objective = "\033[1;33m#\033[m"
objectivePosition = random.randint(1, 49)
enemy = "\033[1;31mX\033[m"
enemyPosition = random.randint(1, 49)
while enemyPosition != objectivePosition:
    objectivePosition = random.randint(1, 49)
    enemyPosition = random.randint(1, 49)

# Menu inicial
print("-=" * 35)
print("Olá, seja bem vindo!")
print("Abaixo está a lista com as letras que representam o movimento!")
while True:

    # O tabuleiro bruto
    line0 = ["\n", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "\n",
             10, 11, 12, 13, 14, 15, 16, 17, 18, 19, "\n",
             20, 21, 22, 23, 24, 25, 26, 27, 28, 29, "\n",
             30, 31, 32, 33, 34, 35, 36, 37, 38, 39, "\n",
             40, 41, 42, 43, 44, 45, 46, 47, 48, 49]

    print("""
    1 - Iniciar Jogo
    2 - Ajuda
    3 - Opções""")
    opcaoInicial = input("Insira a opção desejada: ")
    if opcaoInicial not in "12":
        print("Opção Inválida!")
    if opcaoInicial == "3":
        menuOpcao()
    if opcaoInicial == "2":
        menuAjuda()
    if opcaoInicial == "1": break;

print("BOA SORTE!")
print("-=" * 35)

# coisas para adicionar: inimigo, opção do objetivo andar, teleporte, salvar,
# menu de ajudas,


# inicio do jogo
while playerPosition != objectivePosition:

    # Colocando cada "objeto" em seu lugar no tabuleiro.
    for p in range(len(line0)):
        line0[p] = player if line0[p] == playerPosition else line0[p]
        line0[p] = objective if line0[p] == objectivePosition else line0[p]

    # Criando a parte visual do tabuleiro
    tabuleiro = list()
    for n in range(len(line0)):
        tabuleiro.append(str(line0[n]))
    for n in tabuleiro:
        if n != player and n != objective and n != "\n" and int(n) < 10:
            n = "[ ]"
        elif n == player and n != "\n":
            n = "[" + player + "]"
        elif n == objective and n != "\n":
            n = "[" + objective + "]"
        elif n != "\n":
            n = "[ ]"
        print(n, end=" ")
    print()

    # Loop para o jogador escolher a direção, aceitando apenas WASD
    while True:

        move = input("Para onde deseja se mover? ").upper()
        if move in "WASD":
            if move == "W":
                nova_posicao = move_up(playerPosition)
            if move == "D":
                nova_posicao = move_right(playerPosition)
            if move == "S":
                nova_posicao = move_down(playerPosition)
            if move == "A":
                nova_posicao = move_left(playerPosition)

            if verificarMovimento(nova_posicao) == True:
                print("Não é possível sair do mapa..")
            else:
                break
        else:
            print("Opção inválida")

    # Movendo o "objeto" jogador
    if move == "W":
        retornar()
        playerPosition = move_up(playerPosition)
    elif move == "D":
        retornar()
        playerPosition = move_right(playerPosition)
    elif move == "S":
        retornar()
        playerPosition = move_down(playerPosition)
    else:
        retornar()
        playerPosition = move_left(playerPosition)

# Ultima reformulação antes de fechar o game
for p in range(len(line0)):
    line0[p] = player if line0[p] == playerPosition else line0[p]
    line0[p] = objective if line0[p] == objectivePosition else line0[p]

tabuleiro = list()
for n in range(len(line0)):
    tabuleiro.append(str(line0[n]))
for n in tabuleiro:
    if n != player and n != objective and n != "\n": n = "[ ]";
    elif n == objective and n != "\n": n = "["+player+"]";
    elif n == player and n != "\n": n = "["+player+"]";
    elif n != "\n": n = "[ ]";
    print(n, end=" ")
print()

print("MEUS PARABÉNS, VOCÊ GANHOU!")
# Fim do jogo

