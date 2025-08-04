print('Aula09_1ªparte')
print(""" Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos aprender são o Fatiamento de String, Análise com len(), )
   count(), find(), transformações com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join().""")
frase = "Python é incrível"
print(frase[0:6])    # Python
print(frase[7:9])    # é
print(frase[-8:])    # incrível
print(len(frase))    # 17
print(frase.count('i'))  # 2
print(frase.find('é'))   # 7
print(frase.find('Java')) # -1 (não encontrado)
print(frase.replace('incrível', 'fantástico'))
# Python é fantástico
print(frase.upper())     # PYTHON É INCRÍVEL
print(frase.capitalize())  # Python é incrível
nome = "  Andre  "
print(nome.strip())        # Andre
print(nome.rstrip())       # "  Andre"
print(nome.lstrip())       # "Andre  "
palavras = ['Python', 'é', 'legal']
print(' '.join(palavras))  # Python é legal
texto = "  Olá mundo Python  "
print(texto.strip().title().replace("Python", "3.12"))
# Olá Mundo 3.12
print(' ')
print('Aula09_2ªparte')
print('==='*50)
print('--> Versão Guanabarra:')
frase = 'boa noite,'
print(frase)
frase1 = 'programadores'
print(frase1[3:4])
frase2 = 'curso em video'
print(frase2[1:15:2])
frase3 = ' Desenvovlvimento Full Stack '
print(frase3)
print(len(frase3))
print(len(frase3.strip()))
# frase3(0) = 'J'
print(frase3)
# frase3 = frase3.replace('JS', 'ReactCVite', 'PHP')
# print(frase3)


print('==='*50)
print('The End.')