soma = 0
contador = 0

for c in range(3, 501, 3):
    if c % 2 != 0:
        contador = contador + 1
        soma = soma + c

print(f'A soma de todos os {contador} valores solicitados é {soma}')
