# Operadores_Artimeticos
print('---  Operadores_Artimeticos-- ')
print('5 + 2 =',5 + 2 )
print('5 - 2 =',5 - 2)
print('5 * 2 =',5 * 2)
print('5 / 2 =', 5 / 2)
print('5 ** 2 = ', 5 ** 2)
print('5 // 2 =',5 // 2)
print('5 / 2 = ', 5 / 2)
print('Ordem Precedência:')
print('1ª ()')
print('2ª **')
print('3ª * / // /')
print('4ª + -')
print('Bora pratica:')
print('5 + 3 * 2 =', 5 + 3 * 2)
print('3 * 5 + 4 ** 2 =', 3 * 5 + 4 ** 2)
print('3 * ( 5 + 4) ** 2 =', 3 * (5 + 4) ** 2)
print('Hora da prática:')
# nome = input('Qual é seu nome?')
# print('Prazer em te conhecer sr(ª){:>20}!'.format(nome))
nome = input('Informe o nome do aluno:')
print('As notas do aluno:{}!'.format(nome),'são:')
n1 = int(input('Soma 01 é = '))
n2 = int(input('Soma 02 é = '))
s = n1 + n2
m = n1 * n2 
d = n1  / n2
di = n1 // n2
e = n1 ** n2 
print('A soma é {} ,\n o produto é {}, \n e a divisão é {}'.format(s, m, d), end=' ')
print('Divisão inteira é {},potência {}'.format(di, e))
print('The End')