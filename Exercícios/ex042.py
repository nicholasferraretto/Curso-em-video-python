a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima podem formar um triângulo', end=' ')
    if a == b == c:
        print('equilátero')
    elif a != b != c != a:
        print('escaleno')
    else:
        print('isósceles')
else:
    print('Os segmentos acima não podem formar um triângulo')
