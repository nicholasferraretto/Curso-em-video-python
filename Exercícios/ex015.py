km = float(input('Quantos km rodados: '))
dias = int(input('Quantos dias alugados? '))
total = (60 * dias) + (0.15 * km)
print('O total a pagar é de {:.2f}'.format(total))
