# Operações aritméticas

# teoria
"""
+ : Adição  (5 + 2 == 7)
- : Subtração  (5 - 2 == 3)
* : Multiplicação  (5 * 2 == 10)
/ : Divisão  (5 / 2 == 2.5)
** : Potência  (5 ** 2 == 25)
// : Divisão inteira  (5 // 2 == 2)
% : Resto da divisão ou módulo  (5 % 2 == 1)
"""

# Ordem de precedência
"""
1) ()
2) **
3) *, /, //, %
4) +, -
"""

# 1
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro: '))
soma = n1 + n2
multiplicação = n1 * n2
divisão = n1 / n2
divisãoint = n1 // n2
potência = n1 ** n2
print('A soma é {}, o produto {} e a divisão é {:.2f}'.format(soma, multiplicação, divisão))
print('Divisão inteira {} e a potência {}'.format(divisãoint, potência))
