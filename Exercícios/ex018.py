from math import sin, cos, tan, radians
x = float(input('Digite o ângulo que você deseja: '))
sen = sin(radians(x))
cosseno = cos(radians(x))
tg = tan(radians(x))
print('''
O ângulo de {} tem o seno de {:.2f}
O ângulo de {} tem o cosseno de {:.2f}
O ângulo de {} tem a tangente de {:.2f}
'''.format(x, sen, x, cosseno, x, tg))
