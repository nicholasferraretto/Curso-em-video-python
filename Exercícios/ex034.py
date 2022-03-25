salário = float(input('Qual o salário do funcionário? R$ '))
if salário <= 1250:
    aumento = salário * 1.15          # 15%
else:
    aumento = salário * 1.1           # 10%
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salário, aumento))
