print('Aula 20 – Funções (Parte 2)_1ªparte')
print("""
Nessa aula, vamos continuar nossos estudos de funções em Python, aprendendo mais sobre Interactive Help em Python, o uso de docstrings para documentar nossas funções, 
      argumentos opcionais para dar mais dinamismo em funções Python, escopo de variáveis e retorno de resultados.
""")
print('=====Exercicios====='*8)
print(help)
print("""
Funções em Python – Parte 2

Nesta aula, vamos aprofundar nossos estudos sobre funções em Python, explorando alguns recursos que tornam o código mais organizado, reutilizável e fácil de manter.

O Interactive Help do Python é uma ferramenta útil que nos permite consultar a documentação de funções, classes e módulos diretamente no terminal. Com o comando help(), podemos verificar rapidamente como utilizar determinado recurso da linguagem. Por exemplo, ao executar help(print), temos acesso à explicação completa sobre a função print. Outra forma é acessar diretamente a propriedade __doc__ de uma função.

Outro recurso importante são as docstrings, que servem para documentar nossas funções. Elas são escritas logo abaixo da declaração da função, entre aspas triplas, e ajudam tanto quem programa quanto outras pessoas que futuramente precisarão entender o código. Além disso, quando usamos help() em uma função que possui docstring, o Python mostra automaticamente a documentação que escrevemos.

Também podemos tornar nossas funções mais flexíveis com o uso de argumentos opcionais. Isso significa definir valores padrão para os parâmetros, 
      de forma que, caso o usuário não forneça algum valor, a função utiliza o valor definido por padrão. Assim, evitamos erros e deixamos a função mais dinâmica.

Outro ponto essencial é o escopo de variáveis. Variáveis podem ser locais,
 quando são criadas dentro de uma função e só podem ser usadas nela, ou globais, quando estão disponíveis em todo o programa. É importante entender essa diferença para evitar conflitos e erros inesperados. Em alguns casos, podemos precisar alterar uma variável global dentro de uma função, e para isso utilizamos a palavra-chave global.

Por fim, as funções podem devolver resultados através da instrução return. Com ela, podemos processar informações dentro da função e retornar valores para serem armazenados em variáveis ou utilizados em outras operações.
 Essa prática é fundamental para a construção de programas mais complexos, pois permite dividir o problema em pequenas partes reutilizáveis.

Em resumo, nesta aula aprendemos a usar o help interativo, a escrever docstrings para documentar funções, a trabalhar com argumentos opcionais, a entender melhor o escopo das variáveis e a utilizar o retorno de resultados com return. Esses conceitos são fundamentais para escrever códigos mais claros, organizados e eficientes em Python.
""")
print(input.__doc__)
def contador(i, f,p):
    """""
    TO.....
    """
    c = i
    while c <= f:
        print(f'{c}',end='')
        c += p
    print('fim')
help(contador) 

print('The End')