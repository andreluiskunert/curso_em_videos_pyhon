# Exercicio:09
print(' Exercicio:09')
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
print('==='*50)
print('-->Versão Guanabarra:')
salario = float(input('Qual éo salário do funcionario? R$ '))
novo = salario +( salario * 15 /100)
print('Um funcionário que ganhava R${:.2f}, com o desconto de 15% de aumento,passará a receber R${}'.format(salario, novo))


print('==='*50)
print('')
print('The End')