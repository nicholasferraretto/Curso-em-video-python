# minha resolução por encaminhamento matemático
"""
num = int(input('Digite um número: '))
if num == 2 or num == 3 or num == 5 or num == 7:
    print(f'O número {num} é primo')
elif num % 2 != 0 and num % 3 != 0 and num % 5 != 0 and num % 7 != 0:
    print(f'O número {num} é primo')
else:
    print(f'O número {num} não é primo')
"""

num = int(input('Digite um número: '))
total = 0
red = '\033[1;31m'
yellow = '\033[1;33m'
limpa = '\033[m'

for c in range(1, num + 1):
    if num % c == 0:
        print(f'{yellow}', end='')
        total += 1
    else:
        print(f'{red}', end='')
    print(c, end=' ')

print(f'\n{limpa}O número {num} foi divisível {total} vezes')

if total == 2:
    print('E por isso ele é primo!')
else:
    print('E por isso ele não é primo!')
