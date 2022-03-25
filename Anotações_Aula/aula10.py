# Condições simples e compostas

# 1(condição simples)
nome = str(input('Qual é o seu nome? ')).strip().lower()
if nome == 'nicholas':
    print('Que nome lindo você tem')
print('Bom dia, {}!'.format(nome))

# 2(condição composta)
tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')

"""
Forma simplificada (Operador ternário em outras linguagens)
tempo = int(input('Quantos anos tem seu carro? '))
print('Carro novo' if tempo <=3 else 'Carro velho')
"""

# 3
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
média = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(média))
if média >= 6.0:
    print('Sua média foi boa, parabéns!')
else:
    print('Sua média foi ruim, estude mais!')
