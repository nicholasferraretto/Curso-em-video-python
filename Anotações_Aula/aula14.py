# Estrutura de repetição while

# 1(Usando while com limite)
c = 1
while c < 10:
    print(c)
    c += 1
print('FIM')

# 2(Enquanto não digitar zero não para)
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')

# 3
resposta = 'S'
while resposta == 'S':
    n = int(input('Digite um valor: '))
    resposta = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')

# 4
n = 1
pares = 0
ímpares = 0
# par = ímpar = 0 (Outra forma de fazer)
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            pares += 1
        else:
            ímpares += 1
print(f'Foram digitados {pares} números pares e {ímpares} números ímpares ')
