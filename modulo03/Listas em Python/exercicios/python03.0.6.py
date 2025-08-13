print('06)Exercicios_Validando expressões matemáticas')
print(""" 
 Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
      Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
""")
# Exercício Python 083

expressao = input("Digite uma expressão: ")

pilha = []  # Usamos uma lista como pilha para controlar os parênteses

for simbolo in expressao:
    if simbolo == "(":
        pilha.append("(")  # Empilha quando abre parêntese
    elif simbolo == ")":
        if len(pilha) > 0:
            pilha.pop()  # Remove um parêntese da pilha
        else:
            pilha.append(")")  # Parêntese fechado sem abrir antes
            break

if len(pilha) == 0:
    print("Expressão válida ✅")
else:
    print("Expressão inválida ❌")
print('-x-x-'*20)
print('Versão Guanabarra: ')
expr = str(input('Informe a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida: ')
else:
    print('Sua expresão está errada: ')

print('--=--'*15)
print('==>=='*20)
print('The End')