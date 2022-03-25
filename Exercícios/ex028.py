from random import randint
from time import sleep

red = '\033[1;31m'
yellow = '\033[1;33m'
blue = '\033[1;34m'
limpa = '\033[m'
magenta = '\033[1;35m'
computador = randint(0, 5)  # sorteia um valor

print('{}-=-{}'.format(yellow, limpa) * 20)
print('{}Vou pensar em um número entre 0 a 5. Tente adivinhar...{}'.format(blue, limpa))
print('{}-=-{}'.format(yellow, limpa) * 20)

jogador = int(input('Em que número pensei? '))    # jogador escolhe um número
print('{}Processando...{}'.format(magenta, limpa)), sleep(1)

if computador == jogador:
    print('{}Parabéns! Você conseguiu me vencer!'.format(yellow))
else:
    print('{}Ganhei! Eu pensei no número {} e não no {}!'.format(red, computador, jogador))
