a = int(input('Primeiro segmento: '))
b = int(input('Segundo segmento: '))
c = int(input('Terceiro segmento: '))

if a < b + c and b < a + c and c < a + b:
    forma = 'PODEM FORMAR'
    if a == b == c:
        tipo = 'EQUILÁTERO'
    elif a != b != c and a != c:
        tipo = 'ESCALENO'
    else:
        tipo = 'ISÓSCELES'
else:
    forma = 'NÃO PODEM FORMAR'
    tipo = ''

print(f'Os segmentos acima {forma} um triângulo {tipo}')
