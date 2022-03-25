contador = homens = mulheres = 0

while True:
    print('-' * 40)
    print('{:^40}'.format('Cadastre uma pessoa'))
    print('-' * 40)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()
    if idade > 18:
        contador += 1
    if sexo == 'M':
        homens += 1
    elif sexo == 'F':
        if idade < 20:
            mulheres += 1
    opção = ' '
    while opção not in 'SN':
        opção = str(input('Quer continuar[S/N]: ')).strip().upper()
    if opção == 'N':
        break
print(f'{contador} pessoas tem mais de 18 anos'
      f'\n{homens} homens foram cadastrados'
      f'\n{mulheres} mulheres tem menos de 20 anos')
