largura = float(input('Qual a largura da parede(m): '))
altura = float(input('Qual a altura da parede(m): '))
área = largura * altura
tinta = área / 2   # 2m² para cada litro
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(largura, altura, área))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))
