from math import hypot
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjascente: '))
print('O triângulo tem hipotenusa {:.2f}'.format(hypot(co, ca)))

# forma matemática
"""
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjascente: '))
hipotenusa = ((co**2) + (ca**2)) ** (1/2)
print('O triângulo tem hipotenusa {:.2f}'.format(hipotenusa))
"""
