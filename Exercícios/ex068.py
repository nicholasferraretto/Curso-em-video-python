from random import randint

print('=-' * 20)
print('{:^40}'.format('Vamos jogar par ou ímpar'))
print('=-' * 20)

contador = 0
red = '\033[1;31m'
blue = '\033[1;34m'
limpa = '\033[m'

while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    opção = ' '
    while opção not in 'PI':
        opção = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    resto = total % 2
    if resto == 0:           # condições assim são melhores com operador ternário
        pi = 'PAR'           # pi = par ou ímpar
    else:
        pi = 'ÍMPAR'
    print('-' * 70)
    print(f'Você jogou {jogador} e o computador {computador}. '
          f'Total de {total} deu {pi}')
    print('-' * 70)
    if opção == 'P' and resto == 0:
        print(f'{blue}Você venceu!')
        print(f'Vamos jogar novamente...{limpa}')
        print('=-' * 20)
        contador += 1
    elif opção == 'I' and resto != 0:
        print(f'{blue}Você venceu!')
        print(f'Vamos jogar novamente...{limpa}')
        print('=-' * 20)
        contador += 1
    elif opção == 'P' and resto != 0:
        print(f'{red}Você perdeu !{limpa}')
        print('=-' * 20)
        break
    elif opção == 'I' and resto == 0:
        print(f'{red}Você perdeu !{limpa}')
        print('=-' * 20)
        break

print(f'{red}Game over! Você venceu {contador} vezes.')
