print('Exercicio05 – Lista de Preços com Tupla')
print("""
 Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
       No final, mostre uma listagem de preços, organizando os dados em forma tabular.
 """)
print('-x-x-'*20)
# Tupla única com produtos e preços
produtos = (
    'Lápis', 1.75,
    'Borracha', 2.00,
    'Caderno', 15.90,
    'Estojo', 25.00,
    'Transferidor', 4.20,
    'Compasso', 9.99,
    'Mochila', 120.32,
    'Canetas', 22.30,
    'Livro', 34.90
)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)

# Percorre a tupla pulando de 2 em 2
for pos in range(0, len(produtos), 2):
    nome = produtos[pos]
    preco = produtos[pos + 1]
    print(f'{nome:.<30}R$ {preco:>7.2f}')

print('-' * 40)


print('-x-x-'*20)
print('Versão Guanabarra:')
listagem = ('Lápis', 1.75, 
            'Borracha', 2.00,
            'Caderno', 15.90,
           'Estojo', 25.00,
          'Transferidor', 4.20,
          'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.30,
         'Livro', 34.90  )
print('--'*25)
print('Listagem de preços:')
print('--'*25)
for pos in range(0, len(listagem)):
  if pos % 2 == 0:
    print(f'{listagem[pos]:.<30 }', end='')
  else:
     print(f'R${listagem[pos]:>7}')

# print('-x-x-'*20)

print('The End')