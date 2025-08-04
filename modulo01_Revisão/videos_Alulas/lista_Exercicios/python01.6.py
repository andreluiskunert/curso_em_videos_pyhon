#Exercicios06
print('Exercicios06')
print('Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar,considere que U$$1,00= R$3,27')
# Lê o valor em reais que a pessoa tem
reais = float(input("Quanto dinheiro você tem na carteira (em R$)? "))

# Taxa de câmbio fixa
taxa_dolar = 3.27

# Converte reais para dólares
dolares = reais / taxa_dolar

# Mostra o resultado
print(f"Com R${reais:.2f} você pode comprar US${dolares:.2f}.")
print('*******'*20)
print('--> Versão Guanabarra:')
real = float(input('Quanto dinheiro você tem na carteira? '))
dolar = real / 3.27
print('Quanto tantos R${:.2f} você pode comprar U$${:.2f} .'.format(real, dolar))
print('*******'*20)
print('The End')