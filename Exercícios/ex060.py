# Usando a biblioteca math
"""
from math import factorial
num = int(input('Digite um número para calcular seu fatorial: '))
print(f'O fatorial de {num} é igual a {factorial(num)}')
"""

# Usando while
num = int(input('Digite um número para \ncalcular seu fatorial: '))
contador = num
fatorial = 1  # não influenciar no valor da multiplicação

print(f'Calculando {num}! = ', end='')
while contador > 0:
    print(f'{contador}', end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial = fatorial * contador  # mesmo que (fatorial *= contador)
    contador = contador - 1   # mesmo que (contador -= 1)
print(f'{fatorial}')
print('')

# Usando for
n = int(input('Digite outro número para \ncalcular seu fatorial: '))
f = 1

print(f'Calculando {n}! =', end=' ')
for c in range(num, 0, -1):
    print(c, 'x' if c > 1 else '=', end=' ')
    f *= c
print(f)
