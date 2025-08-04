# Desafio01
print('Desafio01: ')
print('Faça um programa em python que leia uma numero inteiro e mostre em tela o seu sucesso e o seu antecessor:')
# Solicita ao usuário que digite um número inteiro
numero = int(input("Digite um número inteiro: "))

# Calcula o antecessor e o sucessor
antecessor = numero - 1
sucessor = numero + 1

# Exibe os resultados
print(f"O número digitado foi {numero}.")
print(f"O antecessor de {numero} é {antecessor}.")
print(f"O sucessor de {numero} é {sucessor}.")
# Desafio01.02

print(' Desafio01.02')
print('Crie um algoritmo que leia um número e mostre o seu dobro,triplo e a raiz quadrada:')
# Solicita ao usuário que digite um número
numero = float(input("Digite um número: "))

# Calcula o dobro, o triplo e a raiz quadrada
dobro = numero * 2
triplo = numero * 3
raiz_quadrada = numero ** 0.5  # ou use: math.sqrt(numero) com import math

# Exibe os resultados
print(f"O número digitado foi {numero}.")
print(f"O dobro de {numero} é {dobro}.")
print(f"O triplo de {numero} é {triplo}.")
print(f"A raiz quadrada de {numero} é {raiz_quadrada:.2f}.")
# Desafio01.03
print(' Desafio01.03')
print('Desenvolva um programa que leia duas medias de um aluno,calcule e mostre a sua media e se caso e ele reprovo, ficou em recuperação ou passou:')
# Lê as duas notas do aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Calcula a média
media = (nota1 + nota2) / 2

# Mostra a média
print(f"A média do aluno é {media:.2f}")

# Verifica a situação do aluno
if media >= 7.0:
    print("Aluno APROVADO!")
elif media >= 5.0:
    print("Aluno em RECUPERAÇÃO.")
else:
    print("Aluno REPROVADO.")

# Desafio01.04
print('Escreva um programa que leia um valor em metros e o exiba convertido em centrimetros em milimetros:')
# Lê o valor em metros
metros = float(input("Digite o valor em metros: "))

# Converte para centímetros e milímetros
centimetros = metros * 100
milimetros = metros * 1000

# Mostra os resultados
print(f"\n{metros} metros equivalem a:")
print(f"{centimetros} centímetros")
print(f"{milimetros} milímetros")

# Desafio01.05
print('Desafio01.05')
print('Faça um programa que leia um numero Inteiro qualquer e mostra na tela sua tabuada:')
# Lê um número inteiro do usuário
numero = int(input("Digite um número inteiro: "))

# Mostra a tabuada de 1 a 10
print(f"\nTabuada do {numero}:\n")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

# Desafio01.06
print(' Desafio01.06')
print('Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar,considere que U$$1,00= R$3,27')
# Lê o valor em reais que a pessoa tem
reais = float(input("Quanto dinheiro você tem na carteira (em R$)? "))

# Taxa de câmbio fixa
taxa_dolar = 3.27

# Converte reais para dólares
dolares = reais / taxa_dolar

# Mostra o resultado
print(f"Com R${reais:.2f} você pode comprar US${dolares:.2f}.")
# Desafio01.07
print('Desafio01.07 ')
print('Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade de tinta para pinta-la,sabendo que cada litro de tinta, pinta uma área de 2m²')
# Lê a largura e a altura da parede
largura = float(input("Digite a largura da parede em metros: "))
altura = float(input("Digite a altura da parede em metros: "))

# Calcula a área
area = largura * altura

# Calcula a quantidade de tinta necessária (1 litro para cada 2 m²)
tinta = area / 2

# Mostra os resultados
print(f"\nA parede tem {largura}m de largura e {altura}m de altura.")
print(f"A área total é de {area:.2f} m².")
print(f"Você precisará de {tinta:.2f} litros de tinta para pintá-la.")
# Desafio01.08
print(' Desafio01.08')
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
# Desafio01.09
print(' Desafio01.09')
print('Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento:')
# Lê o salário atual do funcionário
salario = float(input("Digite o salário atual do funcionário (R$): "))

# Calcula o valor do aumento e o novo salário
aumento = salario * 0.15
novo_salario = salario + aumento

# Mostra os resultados
print(f"\nSalário atual: R${salario:.2f}")
print(f"Aumento de 15%: R${aumento:.2f}")
print(f"Novo salário: R${novo_salario:.2f}")



print('The End')