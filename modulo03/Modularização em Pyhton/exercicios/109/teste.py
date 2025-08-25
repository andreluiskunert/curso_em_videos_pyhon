import moeda
preco = float(input('Informe o preço : R$ ' ))
print(f'§ A metade de {moeda.moeda(preco)} e {moeda.metade(preco, True)}; ')
print(f'§ O dobro  de {moeda.moeda(preco)} e {moeda.dobro(preco,True)}; ')
print(f'§ Aumentando 10% de {moeda.moeda(preco)},temos {moeda.aumentar(preco, 10, True)}; ')
print(f'Reduzindo 13% de {moeda.moeda(preco)} e temos R${moeda.diminuir(preco, 13,True)}; ')