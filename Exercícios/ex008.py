num = float(input('Uma distância em metros: '))
print('A medida de {}m corresponde a'.format(num))
print('{}km'.format(num/1000))
print('{}hm'.format(num/100))
print('{}dam'.format(num/10))
print('{}dm'.format(num*10))
print('{}cm'.format(num*100))
print('{}mm'.format(num*1000))

# Outra forma
print('''A medida de {}m corresponde a 
{}km
{}hm
{}dam
{}dm
{}cm
{}mm
'''.format(num, num/1000, num/100, num/10, num*10, num*100, num*1000))
