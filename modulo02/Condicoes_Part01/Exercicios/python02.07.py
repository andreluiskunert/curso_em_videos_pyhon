# Condições_parte01ª
print(' Aumentos múltiplos')
print('Exerc.06')
print("""  Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
       Para salários superiores a R$1250,00, calcule um aumento de 10%. 
      Para os inferiores ou iguais, o aumento é de 15%. """)

# Solicita o salário atual do funcionário
salario = float(input("Digite o salário do funcionário: R$ "))

# Verifica se o salário é maior que R$1250,00
if salario > 1250:
    aumento = salario * 0.10  # 10% de aumento
else:
    aumento = salario * 0.15  # 15% de aumento

# Calcula o novo salário
novo_salario = salario + aumento

# Exibe o resultado
print(f"O aumento será de R$ {aumento:.2f}")
print(f"O novo salário será de R$ {novo_salario:.2f}")

print('-----'*25)
print('Exemplos Guanabarra:')
# print('1ªEx.:')
salario = float(input('Qual é o salário de funcionário ? '))
if salario <= 1250:
    novo = salario +  (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora . '.format(salario, novo))    


# print('2ªEx.:')

print('-----'*25)
print('The End')