resp = 'S'
contador = soma = maior = menor = 0

while resp in 'S':
    num = int(input('Digite um número: '))
    contador += 1
    soma += num
    if contador == 1:
        maior = menor = num         # mesmo que maior = 0; menor = 0
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
média = soma / contador

print(f'Você digitou {contador} números e a média foi {média:.2f}'
      f'\nO maior valor foi {maior} e o menor foi {menor}')
