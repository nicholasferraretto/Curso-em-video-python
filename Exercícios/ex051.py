print('=' * 30)
print('{:^30}'.format('10 TERMOS DE UMA P.A'))
print('=' * 30)

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = (primeiro + (10 - 1) * razão)       # An = A1 + (n - 1) * r -> termo geral P.A

for pa in range(primeiro, (décimo + razão), razão):
    print(f'{pa}', end=' -> ')

print('FIM')
