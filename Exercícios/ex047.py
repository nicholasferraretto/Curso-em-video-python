print('Os números pares que estão entre 1 e 50 são:')
"""
for n in range(1, 51):           # dessa forma o computador realiza iterações para todos os números
    if n % 2 == 0:               # Ocupa mais memória, faz mais ações(evitar)
        print(n, end=' ')
"""

for n in range(2, 51, 2):
    print(n, end=' ')
