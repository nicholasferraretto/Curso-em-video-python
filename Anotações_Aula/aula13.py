# Estrutura de repetição for

# 1(repetindo uma str)
"""
for c in range(1, 6):             # (1, 6) = 1 a 5; sempre para no anterior
    print('Oi')
print('FIM')
"""

# 2(print na variável de controle - contador)
"""
for c in range(0, 6):
    print(c)
"""

# 3(contando ao contrário)
"""
for c in range(0, 6, -1):        # (início/fim/passo)
    print(c)                     # (0, 7, 2): pulando de dois em dois
"""

# 4(usando variável dentro do for)
"""
n = int(input('Digite um número: '))
for c in range(0, n + 1):
    print(c)
print('FIM')
"""

# 5(outro exemplo)
"""
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f + 1, p):
    print(c)
"""

# 6(Usando input dentro do for)
s = 0
for c in range(0, 4):
    n = int(input('Digite um número: '))
    s = s + n    # ou  s += n
print(f'O somatório de todos os valores foi {s}')
