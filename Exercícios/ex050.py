soma = 0
contador = 0

for x in range(1, 7):
    num = int(input(f'Digite o {x}º valor: '))
    if num % 2 == 0:
        soma += num
        contador += 1

print(f'Você informou {contador}', end=' ')
print('{} e a soma é {}'.format('número par' if contador == 1 else 'números pares', soma))
