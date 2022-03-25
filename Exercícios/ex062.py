print('{:-^30}'.format('Gerador de P.A'))
n1 = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
contador = 1
termo = n1
total = 0
mais = 10

while mais != 0:
    total += mais
    while contador <= total:
        print(termo, end=' -> ')
        contador += 1
        termo += razão
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')
