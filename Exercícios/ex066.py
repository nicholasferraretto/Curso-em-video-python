contador = soma = 0

while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    contador += 1
    soma += n
print(f'A soma dos {contador} valores foi {soma}!')
