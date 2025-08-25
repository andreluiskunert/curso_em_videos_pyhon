import moeda
preco = float(input('Informe o preço : R$ ' ))
print(f'§ A metade de {moeda.moeda(preco)} e {moeda.metade(preco)};')
print(f'§ O dobro  de {moeda.moeda(preco)} e {moeda.dobro(preco)};')
print(f'§ Aumentando 10% de {moeda.moeda(preco)},temos {moeda.aumentar(preco, 10)};')
# print(f'Dimunir  de R${preco} e temos R${moeda.diminuir(preco)};')