# Interrompendo repetições while e f strings

# 1(While infinito)
"""
contador = 1
while True:
    print(contador, '->', end=' ')
    contador += 1
"""

# 2
n = soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
print(f'A soma é {soma}')

print('')

# 3(f string)
nome = 'José'
idade = 33
salário = 987.3
x = 'LOJA'
print(f'O {nome} tem {idade} anos e ganha {salário:.2f}.')
print(f'{x:-^10}')
