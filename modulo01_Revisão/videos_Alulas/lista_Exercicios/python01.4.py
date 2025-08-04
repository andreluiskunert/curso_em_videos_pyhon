# Exercicio.04
print('Exercicio.04')
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
print('--> Versão Guanabarra:')
medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 10000
print('A medida de {} um corresponde a {:.0f}cm e {:.0f}mm .'.format(medida, cm, mm))
print('The End')