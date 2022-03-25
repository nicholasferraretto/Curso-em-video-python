# Tipos primitivos e saída de dados

# teoria
"""
int(7, -4, 0, 9875)
float(4.5, 0.076, -15.223, 7.0)
bool(True, False)
str('Olá', '7.5', '')
"""

# 1
"""
Usando format:
print('A soma vale {}'.format(soma))
print(f'A soma vale {soma}')  (nova formatação)
"""

# 2(A leitura do input sempre vem como str caso não seja especificado)
"""
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro: '))
s = n1 + n2
print('A soma entre {} e {} vale {}'.format(n1, n2, s))
"""

# identificação do tipo de uma variável

n = input('Digite algo: ')
print(type(n))
print(n.isupper())
