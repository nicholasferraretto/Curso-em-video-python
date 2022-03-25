red = '\033[1;31m'
limpa = '\033[m'
print(f'{red}-=' * 15)
print('Analisador de triângulos')
print('-=' * 15, f'{limpa}')
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima podem formar um triângulo!')
else:
    print('Os segmentos acima não formam um triângulo!')
