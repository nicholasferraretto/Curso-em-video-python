print('-' * 40)
print('{:^40}'.format('Sequência de Fibonacci'))
print('-' * 40)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1

print('{} -> {}'.format(t1, t2), end='')
contador = 3

while contador <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    contador += 1
print(' -> FIM')
