from time import sleep

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opção = 0
maior = 0

while opção != 5:
    print("""[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa""")
    opção = int(input('>>>>>Qual sua opção: '))
    if opção == 1:
        print(f'A soma entre {n1} e {n2} é {n1 + n2}')
    elif opção == 2:
        print(f'O produto entre {n1} e {n2} é {n1 * n2}')
    elif opção == 3:
        if n1 > n2:
            maior = n2
        elif n2 > n1:
            maior = n2
        print(f'O maior entre {n1} e {n2} é {maior}')
    elif opção == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')

    else:
        print('Opção inválida. Tente novamente')
    print('-=' * 20)
    sleep(2)
print('Fim do programa! Volte sempre')
