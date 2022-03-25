print('{:-^40}'.format(' LOJAS EGASHIRA '))
preço = float(input('Preço das compras: R$ '))
print('''Formas de pagamento
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual a forma de pagamento: '))
if opção == 1:
    total = preço * 0.9   # 10% de desconto
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
elif opção == 2:
    total = preço * 0.95  # 5% de desconto
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
elif opção == 3:
    parcela = preço / 2   # preço se mantém
    print('Sua compra será parcelada em 2x de R${:.2f} sem juros '.format(parcela))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, preço))
elif opção == 4:
    parcela = int(input('Quantas parcelas: '))
    total = preço * 1.2  # 20% de aumento(juros)
    valparcela = total / parcela
    print('Sua compra será parcelada em {}x de R${:.2f} com juros '.format(parcela, valparcela))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
else:
    print('{}Opção não disponível. Tente novamente!'.format('\033[1;31m'))
