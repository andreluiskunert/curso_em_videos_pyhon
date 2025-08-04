# Exercicio.08
print(' Exercicio.08')
print('Faça um algoritmo que leia o preço de um produto mostre seu novo preço, com o desconto de 5% de desconto:')
# Lê o preço original do produto
preco = float(input("Digite o preço do produto (R$): "))

# Calcula o valor com 5% de desconto
desconto = preco * 0.05
novo_preco = preco - desconto

# Mostra os resultados
print(f"\nPreço original: R${preco:.2f}")
print(f"Desconto de 5%: R${desconto:.2f}")
print(f"Novo preço com desconto: R${novo_preco:.2f}")
print('')
print('==='*50)
print('-->Versão Guanabarra:')
preco = float(input('Qual é o preço do produto? R$'))
novo = preco - (preco * 5 / 100)
print('O produto que custava R${:.2f}, na promoção com o deseconto de 5%  vai custar R${:.2f} .'.format(preco, novo))
print('==='*50)
print('')
print('The End')