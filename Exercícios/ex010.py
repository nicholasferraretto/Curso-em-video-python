real = float(input('Quanto dinheiro você têm na carteira? R$'))
dólar = real / 3.27  # dólar em 2017
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dólar))
