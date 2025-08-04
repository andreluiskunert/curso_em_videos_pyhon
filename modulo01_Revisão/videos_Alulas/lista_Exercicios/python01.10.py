# Exercício 10 - Conversão de Celsius para Fahrenheit
print('Exercício.10')
# Entrada de dados
celsius = float(input("Digite a temperatura em graus Celsius: "))

# Conversão
fahrenheit = (celsius * 9/5) + 32

# Saída de dados
print(f"A temperatura de {celsius:.1f}°C corresponde a {fahrenheit:.1f}°F.")
print('==='*50)
print('-->Versão Guanabarra:')
c = float(input('Informe a temperatura em °C: '))
f = ( ( 9*c)  / 5 ) + 32
print('A temperatura de {}°C corresponde a {}°F!'.format(c, f))


print('==='*50)
print('')
print('The End')