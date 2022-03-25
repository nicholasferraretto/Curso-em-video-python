from datetime import date

ano_atual = date.today().year
maiores = 0
menores = 0

for c in range(1, 8):
    nascimento = int(input(f'Em que ano a {c}° pessoa nasceu: '))
    idade = ano_atual - nascimento
    if idade >= 21:
        maiores += 1
    else:
        menores += 1

print(f'Ao todo tivemos {maiores} pessoas maiores de idade'
      f'\nE também tivemos {menores} pessoas menores de idade ')
