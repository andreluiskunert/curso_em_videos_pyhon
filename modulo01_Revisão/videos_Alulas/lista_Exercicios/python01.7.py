# Exercicio.07
print('Exercicio.07 ')
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
print('')
print('--*--*--'*20)
print('-->Versão Guanabarra:')
larg =float(input('Informe a largura da parede:'))
alt = float(input('Informe a altura da parede:'))
area =  larg * alt
print('Sua parede tem a dimensão de {} x {} e sua área é de {}m².'.format(larg, alt, area))
tint = area / 2
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tint))
print('--*--*--'*20)
print('')
print('The End')