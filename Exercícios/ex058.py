from random import randint

red = '\033[1;31m'
blue = '\033[1;34m'
limpa = '\033[m'
computador = randint(0, 10)
jogador = 0
tentativa = 0        # Quando sai 0 da erro

print("""Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
será que você consegue adivinhar qual foi?""")

while jogador != computador:
    jogador = int(input('Qual é o seu palpite? '))
    tentativa += 1
    if jogador > computador:
        print(f'{red}Menos... Tente mais uma vez.{limpa}')
    elif jogador < computador:
        print(f'{red}Mais... Tente mais uma vez.{limpa}')

print(f'{blue}Acertou com {tentativa} tentativas. Parabéns!')
