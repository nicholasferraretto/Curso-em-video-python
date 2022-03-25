total = mil = contador = barato = 0
nb = ' '   # nome do mais barato

print('-' * 80)
print('{:^80}'.format('LOJAS EGASHIRA'))
print('-' * 80)

while True:
    nome = str(input('Nome do produto: ')).strip().capitalize()
    preço = float(input('Preço: R$'))
    total += preço
    contador += 1
    if preço > 1000:
        mil += 1                    # Quando dois blocos são iguais:
    if contador == 1:               # if contador == 1 or preço < barato:
        barato = preço              # barato = preço
        nb = nome                   # nb = nome
    else:
        if preço < barato:
            barato = preço
            nb = nome
    opção = ' '
    while opção not in 'SN':
        opção = str(input('Quer continuar [S/N]: ')).strip().upper()
    if opção == 'N':
        break
print('{:-^40}'.format(' Fim do programa '))
print(f'O total gasto na compra é de R${total:.2f}'
      f'\n{mil} produtos custam mais de R$1000 reais'
      f'\n{nb} que custa R${barato:.2f} é o produto mais barato entre os listados')
