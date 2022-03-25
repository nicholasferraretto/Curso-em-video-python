velocidade = float(input('Qual a velocidade atual do carro: '))
if velocidade > 80:
    multa = 7 * (velocidade - 80)    # 7.00 R$ por km excedido
    print('{}Multado! Você excedeu o limite permitido que é de 80Km/h'.format('\033[1;31m'))
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
else:
    print('Tenha um bom dia! Dirija com segurança!')
