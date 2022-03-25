salário = float(input('Qual o salário do funcionário: R$'))
aumento = salário * 1.15
print('O funcionário que ganhava R${:.2f}, com 15% de aumento'.format(salário), end=' ')
print('passa a ganhar R${:.2f}'.format(aumento))
