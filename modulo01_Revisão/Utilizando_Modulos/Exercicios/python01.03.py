print('Exercicio02')
print('Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.')

import math

# Entrada do usuário
angulo = float(input("Digite o ângulo em graus: "))

# Conversão de graus para radianos
radianos = math.radians(angulo)

# Cálculos trigonométricos
seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)

# Exibição dos resultados
print(f"O ângulo de {angulo}° tem:")
print(f"  Seno     = {seno:.4f}")
print(f"  Cosseno  = {cosseno:.4f}")
print(f"  Tangente = {tangente:.4f}")

print('==='*50)
print('--> Versão Guanabarra:')
import math
angulo = float(input('Informe o angulo que deseja:'))
seno = math.sin(math.radians(angulo))
print('O ângulo de {} tem o SENO {:.2f} .'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2f} .'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O ângulo de {} tem o TANGENTE de {:.2f} .'.format(angulo, tangente))
print('2ªOpção:') 
from math import radians, sin, cos, tan
angulo = float(input('Informe o angulo que deseja:'))
seno = sin(radians(angulo))
print('O ângulo de {} tem o SENO {:.2f} .'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2f} .'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O ângulo de {} tem o TANGENTE de {:.2f} .'.format(angulo, tangente))
print('==='*50)
print('The End.')