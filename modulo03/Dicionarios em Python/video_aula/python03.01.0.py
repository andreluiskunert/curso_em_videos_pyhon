print('Video_Aula:Dicionários_1ªparte')
print("""
Nessa aula, vamos aprender o que são DICIONÁRIOS e como utilizar dicionários em Python. 
      Os dicionários são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves literais.
 """)
print('-x-x-'*20)
print(""" 
Assim como listas e tuplas, os dicionários em Python são estruturas de dados que podem armazenar múltiplos valores.
A diferença é que listas e tuplas usam índices numéricos, enquanto dicionários usam chaves (keys), que podem ser textos (strings), números ou até tuplas imutáveis.

🔑 O que é um Dicionário?

Um dicionário é uma coleção de pares chave → valor.

A chave é única e serve para identificar o dado.

O valor é a informação associada à chave.

👉 A sintaxe básica é:

""")
meu_dicionario = {
    "nome": "Ana",
    "idade": 25,
    "cidade": "São Paulo"
}
print(""" Aqui:

"nome", "idade" e "cidade" são as chaves.

"Ana", 25 e "São Paulo" são os valores.

📌 Como acessar valores de um dicionário"

""")
print(meu_dicionario["nome"])   # Ana
print(meu_dicionario["idade"])  # 25
print("""
⚠️ Se a chave não existir, vai dar erro.
Para evitar isso, pode-se usar .get():
""")
print(meu_dicionario.get("profissao", "Não informado"))
print('Como adicionar ou alterar valores')
meu_dicionario["idade"] = 26  # altera
meu_dicionario["profissao"] = "Engenheira"  # adiciona
print('📌 Como remover valores')
del meu_dicionario["cidade"]  # remove a chave "cidade"
print('📌 Percorrer um dicionário')
for chave, valor in meu_dicionario.items():
    print(f"{chave} → {valor}")
print('Saída:') 
print("""
nome → Ana
idade → 26
profissao → Engenheira
""")
print("""
📖 Exemplo prático

Imagine um sistema para cadastrar alunos:
""")
aluno = {
    "nome": "Carlos",
    "notas": [8.5, 7.0, 9.0],
    "aprovado": True
}

print(aluno["nome"])       # Carlos
print(aluno["notas"])      # [8.5, 7.0, 9.0]
print(aluno["notas"][1])   # 7.0

print("""

👉 Ou seja:

Listas organizam dados em ordem (0, 1, 2...).

Dicionários organizam dados por chaves nomeadas (como se fossem etiquetas).
""")


print('-x-x-'*20)
print('Versão Guanabarra: ')
print('Bora lá pratica...')
pessoas = {'nome':'Andre Luis','sexo':'M','idade':43,'profissao':'Dev Full Stack'}
pessoas['nome'] = 'Andre Luis Kunert'
pessoas['peso'] = 65.0
print(pessoas)
print(f'Meu Nome é {pessoas["nome"]},tenho {pessoas["idade"]} anos,sou {pessoas["profissao"]}')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('==>=='*20)
print('The End')