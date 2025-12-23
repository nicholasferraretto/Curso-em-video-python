# Cores no terminal

# Sintaxe padrão
'''
\033[style;text;backm
'''

# 1
print('\033[1;31;43mOlá, Mundo!\033[m')  # É necessário colocar a cor padrão após alterar
print('\033[7;30mOlá, Mundo!\033[m')     # pois se não pintará td o código

# 2
a = 3
b = 5
print('Os valores são \033[1;33m{}\033[m e \033[1;31m{}\033[m!!!'.format(a, b))

# 3(Ultilizando format)
nome = 'Nicholas'
print('Olá ! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))

# 4(Ultilizando dicionários)
nome = 'Nicholas'
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m'}

print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['azul'], nome, cores['limpa']))
