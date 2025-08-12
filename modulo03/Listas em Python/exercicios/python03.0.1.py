print('01)Exercicios')
print(""" Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, 
      mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
""")
# Exercício Python 078

valores = []

# Entrada de dados
for i in range(5):
    num = int(input(f"Digite o {i+1}º valor: "))
    valores.append(num)

# Determinar maior e menor
maior = max(valores)
menor = min(valores)

# Saída de resultados
print(f"\nVocê digitou os valores: {valores}")
print(f"O maior valor foi {maior} nas posições: ", end="")
for i, v in enumerate(valores):
    if v == maior:
        print(f"{i} ", end="")

print(f"\nO menor valor foi {menor} nas posições: ", end="")
for i, v in enumerate(valores):
    if v == menor:
        print(f"{i} ", end="")

print('-x-x-'*20)
print('Versão Guanabarra: ')
listaNum = []
maior = 0
menor = 0
for c in range(0, 5):
  listaNum.append(  int(input(f'Informe um valor pra a posição {c}ª:')) ) 
  if c == 0:
      maior = menor = listaNum[c]
  else:
      if listaNum[c] > maior:
          maior = listaNum[c]
      if listaNum[c] < menor:
          menor = listaNum[c]
print('-=-'*15)
print(f'Você informou os valores {listaNum}: ')
print(f'O maior valor informado foi {maior}', end='')
for i, v in enumerate(listaNum):
   if v == maior:
      print(f'{i}...', end='')
print('=*=*='*15)
print(f'O menor valor informado foi {menor}',end='')
for i, v in enumerate(listaNum):
   if v == menor:
      print(f'{i}...', end='')
print('==>=='*20)
print('The End')