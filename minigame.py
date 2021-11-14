from random import randint
from menu import *

# Definindo funções


def movimentoInimigo(enemyPosition):
    while True:
        opcaoInimigo = randint(1,4)
        enemyNewPosition = enemyPosition
        if opcaoInimigo == 1: enemyNewPosition -= 10;
        if opcaoInimigo == 2: enemyNewPosition += 1;
        if opcaoInimigo == 3: enemyNewPosition += 10;
        if opcaoInimigo == 4: enemyNewPosition -= 1;
        if enemyNewPosition != "\n" and enemyNewPosition != objectivePosition:
            enemyPosition = enemyNewPosition
            return enemyPosition


def verificarMovimento(nova_posicao, playerPosition, move):
    if (nova_posicao < 0) or (nova_posicao > 49) or \
            ((playerPosition in (9, 19, 29, 39, "\n")) and move == "D") or \
            ((playerPosition in (0, 10, 20, 30, 40, "\n")) and move == "A"):
        return True


def verificarMovimentoInimigo(enemyNewPosition, enemyPosition, move):
    if (enemyNewPosition < 0) or (enemyNewPosition > 49) or \
            ((enemyPosition in (9, 19, 29, 39, "\n")) and move == "D") or \
            ((enemyPosition in (0, 10, 20, 30, 40, "\n")) and move == "A"):
        return True


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


def retornarVazio():
    for c in range(len(line0)):
        if line0[c] == player:
            line0[c] = playerPosition


def retornarVazioInimigo():
    for c in range(len(line0)):
        if line0[c] == enemy:
            line0[c] = enemyPosition


# Definindo variáveis
numeroInimigos = 1

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
    if opcaoInicial not in "123":
        print("Opção Inválida!")
    if opcaoInicial == "3":
        menuOpcao()
    if opcaoInicial == "2":
        menuAjuda()
    if opcaoInicial == "1": break;

# coisas para adicionar:  opção do objetivo andar, teleporte, salvar,


playerPosition = 0
derrota = False
objectivePosition = randint(1, 49)
enemyPosition = randint(1, 49)
while enemyPosition == objectivePosition:
    enemyPosition = randint(1, 49)


print("BOA SORTE!")
print("-=" * 35)

# inicio do jogo
while playerPosition != objectivePosition:

    for p in range(len(line0)):
        line0[p] = player if line0[p] == playerPosition else line0[p]
        line0[p] = objective if line0[p] == objectivePosition else line0[p]
        line0[p] = enemy if line0[p] == enemyPosition else line0[p]

    # Criando a parte visual do tabuleiro
    tabuleiro = list()
    for n in range(len(line0)):
        tabuleiro.append(str(line0[n]))

    for n in tabuleiro:
        if n != player and n != objective and n != enemy and n != "\n" and int(n) < 10:
            n = "[ ]"
        elif n == player and n != "\n":
            n = "[" + player + "]"
        elif n == objective and n != "\n":
            n = "[" + objective + "]"
        elif n == enemy and n != "\n":
            n = "[" + enemy + "]";
        elif n != "\n":
            n = "[ ]"
        print(n, end=" ")
    print()

    if playerPosition == enemyPosition:
        derrota = True
        break
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

            if verificarMovimento(nova_posicao, playerPosition, move):
                print("Não é possível sair do mapa..")
            else:
                break
        else:
            print("Opção inválida")

    # Movendo o "objeto" jogador
    if move == "W":
        retornarVazio()
        playerPosition = move_up(playerPosition)
    elif move == "D":
        retornarVazio()
        playerPosition = move_right(playerPosition)
    elif move == "S":
        retornarVazio()
        playerPosition = move_down(playerPosition)
    else:
        retornarVazio()
        playerPosition = move_left(playerPosition)
    retornarVazioInimigo()
    enemyPosition = movimentoInimigo(enemyPosition)


# Ultima reformulação antes de fechar o game
for p in range(len(line0)):
    line0[p] = player if line0[p] == playerPosition else line0[p]
    line0[p] = objective if line0[p] == objectivePosition else line0[p]

tabuleiro = list()
for n in range(len(line0)):
    tabuleiro.append(str(line0[n]))

print()

if derrota:
    for n in tabuleiro:
        if n != player and n != objective and n != enemy and n != "\n" and int(n) < 10:
            n = "[ ]"
        elif n == player and n != "\n":
            n = "[" + enemy + "]"
        elif n == objective and n != "\n":
            n = "[" + objective + "]"
        elif n == enemy and n != "\n":
            n = "[" + enemy + "]"
        elif n != "\n":
            n = "[ ]"
        print(n, end=" ")
    print()
    print("Sinto muito, você perdeu!")
else:
    for n in tabuleiro:
        if n != player and n != objective and n != enemy and n != "\n" and int(n) < 10:
            n = "[ ]"
        elif n == player and n != "\n":
            n = "[" + player + "]"
        elif n == objective and n != "\n":
            n = "[" + player + "]"
        elif n == enemy and n != "\n":
            n = "[" + enemy + "]";
        elif n != "\n":
            n = "[ ]"
        print(n, end=" ")
    print()
    print("MEUS PARABÉNS, VOCÊ GANHOU!")
# Fim do jogo
