# minha resolução
contador = 0
média = 0
mulheres = 0
ihv = 0  # homem mais velho
ndv = 0  # nome do mais velho

for c in range(1, 5):
    print(f'----- {c}ª PESSOA -----')
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    contador += idade
    média = contador / 4
    if sexo == 'M':
        if c == 1:
            ihv = idade
            ndv = nome
        else:
            if idade > ihv:
                ihv = idade
                ndv = nome
    else:
        if idade < 20:
            mulheres += 1

print(f'A média de idade do grupo é de {média:.1f} anos'
      f'\nO homem mais velho tem {ihv} anos e se chama {ndv}.'
      f'\nAo todo são {mulheres} mulheres com menos de 20 anos')
