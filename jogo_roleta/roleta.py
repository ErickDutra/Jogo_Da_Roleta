import random
from time import sleep


def roleta_girando(cores):
    print(random.choice(cores))
    sleep(1)
    print(random.choice(cores))
    sleep(1)
    print(random.choice(cores))
    sleep(1)
    print('...')
    sleep(1)


def ganhador(jogador, maquina, roleta):
    if (jogador == roleta):
        print('Jogador Ganhou')
    elif (maquina == roleta):
        print('Maquina Ganhou')
    elif (jogador == roleta and maquina == roleta):
        print('Empate')
    else:
        print("Jogue Novamente !!!")


cores = ['azul', 'vermelho', 'amarelo', 'verde', 'roxo', 'laranja']

while True:

    roleta = random.choice(cores)
    maquina = random.choice(cores)
    jogador = input("Escolha uma uma das cores da roleta: azul, vermelho, amarelo, verde, roxo, laranja, ou digite sair para finalizar:").lower()
    if jogador == 'sair':
        break
    roleta_girando(cores)
    print("Roleta:" + roleta)
    sleep(1)
    print("Maquina:" + maquina)
    ganhador(jogador, maquina, roleta)
    

