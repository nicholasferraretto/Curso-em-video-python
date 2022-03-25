preço = float(input('Qual o preço do produto: R$'))
desconto = preço * 0.95
print('O produto que custava R${:.2f}, na promoção com 5% de desconto'.format(preço), end=' ')
print('passa a custar R${:.2f}'.format(desconto))
