from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))

# Outra forma
"""
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))
"""
