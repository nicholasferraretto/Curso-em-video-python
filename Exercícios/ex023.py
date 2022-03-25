num = int(input('Digite um número: '))
print('Analisando o número {}'.format(num))
u = num % 10
d = num % 100 // 10
c = num // 100 % 10
m = num // 1000
print('''unidade: {}
dezena: {}
centena: {}
milhar: {}'''.format(u, d, c, m))
