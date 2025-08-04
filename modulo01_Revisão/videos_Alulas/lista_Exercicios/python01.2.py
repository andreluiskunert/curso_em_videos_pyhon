# Exercicio02
print('Exercicio02')
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
# ========////=============
print('Versão guanabarra01:')
n = int(input('Informe um numero:'))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} vale {}.'.format(n, d))
print('O triplo de {} vale{}.A raiz quadrada de {} e igual {}.'.format(n, t, n, r))
print('Versão guanabarra02:')
n = int(input('Informe um numero:'))
print('O dobro de {} vale {}.'.format(n, (n*2)))
print('O triplo de {} vale {}.A raiz quadrada de {} e igual {}.'.format(n, (n*3), n, (n**(1/2))))
print('Versão guanabarra03:')
n = int(input('Informe um numero:'))
print('O dobro de {} vale {}.'.format(n, (n*2)))
print('O triplo de {} vale {}.A raiz quadrada de {} e igual {}.'.format(n, (n*3), n, pow(n,(1/2))))
print('The End')