from time import sleep
while True:
    num = int(input('Digite um número para ver sua tabuada(digite um valor negativo para parar): '))
    if num < 0:
        print('Finalizando...'), sleep(1)
        break
    print('-' * 80)
    for c in range(1, 11):
        print(f'{num} x {c:2} = {num * c}')
    print('-' * 80)
