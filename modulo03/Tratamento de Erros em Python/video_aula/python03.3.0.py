print('Tratamento de Erros e Exceções')
print("""
Nessa aula, vamos ver como o Python permite tratar erros e criar respostas a essas exceções.
       Aprenda como usar a estrutura try except no Python de uma forma simples.
""")

print('-x-x-'*20)
print('Bom dia..Programador')
# print('python  NameError: name 'python' is not defined')
try:
    a = int(input('Númerador: '))
    b = int(input('Denominador: '))
    r = a / b 
except:
    print('Infelizmente deu BO')
else:
    print(f'O resultado entre {a} e {b} é {r:.1f}; ')
finally:
    print('Volte Sempre! Muito Obrigado!!')
print('==>=='*20)
print('The End')