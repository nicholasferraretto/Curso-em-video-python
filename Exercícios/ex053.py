# minha resolução
frase = str(input('Digite uma frase: ')).strip().upper()

frase_sem_espaço = frase.replace(' ', '')
inverso_da_frase = frase[::-1].replace(' ', '')

print(f'O inverso de {frase_sem_espaço} é {inverso_da_frase}')

if frase_sem_espaço == inverso_da_frase:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
