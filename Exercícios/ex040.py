n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno '))
média = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, média))

if média >= 7:
    print('O aluno está aprovado')
elif média < 5:
    print('O aluno está reprovado')
elif 5 <= média < 7:
    print('O aluno está em recuperação')
