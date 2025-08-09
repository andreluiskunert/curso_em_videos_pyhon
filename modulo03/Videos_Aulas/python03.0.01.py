print('Aula 01 – Tuplas_1ªparte')
print("""
Nessa aula, vamos aprender o que são TUPLAS e como utilizar tuplas em Python.
 As tuplas são variáveis compostas e imutáveis que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.
""")
print('-x-x-'*20)
print("Hora de trabalhar nene:")
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pizza')
for comida in lanche:
    print(f'Vou comer {comida}')
print('comi demais')
print('--=--'*20)
print(lanche)
print(lanche[1])
print(lanche[3])
print(lanche[1:3])
print(lanche[-2:])
print(lanche[-3:])
print('Tuplas são imutavéis:')
print(lanche)
# # lanche[1] = 'Café'
# Traceback (most recent call last):
#   File "/home/desenvolvedor/Curso_em_videos/curso_em_videos_pyhon/modulo03/Videos_Aulas/python03.0.0.py", line 17, in <module>
#     lanche[1] = 'Café'
# TypeError: 'tuple' object does not support item assignment
print(lanche[1])
print(len(lanche))
print(lanche)
print('-x-x-'*20)
print('The End')