distância = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(distância))
if distância <= 200:
    preço = 0.5 * distância
else:
    preço = 0.45 * distância
print('E o preço da sua passagem será de R${:.2f}'.format(preço))

# if simplificado (Operador ternário em outras linguagens)
"""
preço = distância * 0.5 if distância <= 200 else distância * 0.45
"""
