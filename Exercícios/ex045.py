from random import randint
from time import sleep

computador = randint(0, 2)
itens = ('Pedra', 'Papel', 'Tesoura')

print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual é a sua jogada? '))

print('JO'), sleep(1)
print('KEN'), sleep(1)
print('PO!!'), sleep(1)
print('-=' * 12)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=' * 12)

if jogador == 0:
    if computador == 0:
        print('Empate')
    elif computador == 1:
        print('Computador vence')
    elif computador == 2:
        print('Jogador vence')

elif jogador == 1:
    if computador == 0:
        print('Jogador vence')
    elif computador == 1:
        print('Empate')
    elif computador == 2:
        print('Computador vence')

elif jogador == 2:
    if computador == 0:
        print('Computador vence')
    elif computador == 1:
        print('Jogador vence')
    elif computador == 2:
        print('Empate')
