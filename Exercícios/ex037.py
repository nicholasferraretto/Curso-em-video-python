num = int(input('Digite um número inteiro: '))
print('''Opções de conversão:
[ 1 ] para binário
[ 2 ] para octal
[ 3 ] para hexadecimal''')
opção = int(input('Qual sua escolha: '))
if opção == 1:
    print('O número {} em binário ficará {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('O número {} em octal ficará {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('O número {} em hexadecimal ficará {}'.format(num, hex(num)[2:]))
else:
    print('Opção não disponível. Tente novamente!')
