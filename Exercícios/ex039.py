# Usando operador ternário para corrigir plural
from datetime import date
nascimento = int(input('Ano de nascimento: '))
ano = date.today().year    # ano atual
idade = ano - nascimento
print(f'Quem nasceu em {nascimento} tem {idade} anos em {ano}.')
if idade > 18:
    passou = idade - 18
    print('Você já deveria ter se alistado há {} {}.'.format(passou, 'ano' if passou == 1 else 'anos'))
    print('Seu alistamento foi em {}.'.format(ano - passou))
elif idade < 18:
    falta = 18 - idade
    print('Ainda faltam {} {} para o alistamento.'.format(falta, 'ano' if falta == 1 else 'anos'))
    print('O seu alistamento será em {}.'.format(falta + ano))
elif idade == 18:
    print('Você tem que se alistar imediatamente!')
