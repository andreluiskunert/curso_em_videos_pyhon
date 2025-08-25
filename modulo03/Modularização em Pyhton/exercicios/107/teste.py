import moeda
preco = float(input('Informe o preço : R$ ' ))
print(f'§ A metade de {preco} e {moeda.metade(preco)};')
print(f'§ O dobro  de {preco} e {moeda.dobro(preco)};')
print(f'§ Aumentando 10% de R${preco},temos R${moeda.aumentar(preco, 10)};')
# print(f'Dimunir  de R${preco} e temos R${moeda.diminuir(preco)};')