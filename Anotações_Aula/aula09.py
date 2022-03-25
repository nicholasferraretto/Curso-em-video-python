# manipulando cadeias de texto

# exemplos

frase = 'Curso em Vídeo Python'
print(frase)
print(frase[:14])
print(frase[1:14:2])
print(frase[::2])
print(frase.count('o'))
print(frase.upper().count('O'))
print(len(frase))
print(frase.replace('Python', 'Android'))
print('Curso' in frase)
dividido = frase.split()
print(dividido[0][0])
print('-'.join(dividido))
