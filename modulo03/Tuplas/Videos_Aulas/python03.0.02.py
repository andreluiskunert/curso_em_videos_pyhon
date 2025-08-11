print('Aula 01 – Tuplas_2ªparte')
print("""
Nessa aula, vamos aprender o que são TUPLAS e como utilizar tuplas em Python.
 As tuplas são variáveis compostas e imutáveis que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.
""")
print('-x-x-'*20)
print("Hora de trabalhar nene:")
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pizza','batata frita')
for comida in lanche:
   print(f'Vou comer {comida}')
for cont in range(0, len(lanche)):
   print(f'Vou comer {lanche[cont]} na posição {cont}')
for comida in lanche:
   print(f'Vou comer {comida} na posição {cont}')
print('comi demais')
print('--=--'*20)
a = (2, 5, 4)
b = (5, 8, 1, 2)
c =a + b # concatenar
print(a)
print(b)
print(c)
print(len(c))
print(c.count(5))
print(c.count(4))
print(c.index(8))
print(c.index(4))
print(c.index(2, 4))
print(c.index(5, 1))
print('-x-x-'*20)
pessoa = ('André Luis', 43, 65.90, 'M', 'Dev Full Stack')
# del(pessoa[0])
print(pessoa)
print('The End')