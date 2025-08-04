print('Exercicio10')
print(""" Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.""")
# Lê o número entre 0 e 9999
numero = int(input("Digite um número de 0 a 9999: "))

# Garante que o número está no intervalo
if 0 <= numero <= 9999:
    # Converte o número para string e preenche com zeros à esquerda se necessário
    numero_str = f"{numero:0>4}"

    # Mostra os dígitos separados
    print("Unidade:", numero_str[3])
    print("Dezena :", numero_str[2])
    print("Centena:", numero_str[1])
    print("Milhar :", numero_str[0])
else:
    print("Número fora do intervalo permitido.")

print('==='*50)
print('--> Versão Guanabarra:')
num =int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}' .format(num))
print('Unidade: {} '.format(u))
print('Dezena: {}'.format(d))
print('Centenas: {}'.format(c))
print('Milhar: {}'.format(m))
# print('2ªOpção:')


print('==='*50)
print('The End.')