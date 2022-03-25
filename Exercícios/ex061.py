print('{:-^30}'.format('Gerador de P.A'))
n1 = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
contador = 1
termo = n1

while contador <= 10:
    print(termo, end=' -> ')
    contador += 1
    termo += razão
print('FIM')
