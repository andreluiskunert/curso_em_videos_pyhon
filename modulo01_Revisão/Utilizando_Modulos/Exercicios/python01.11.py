print('Exercicio11')
print("""Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”. """)
cidade = input("Digite o nome de uma cidade: ").strip()

# Verifica se começa com "SANTO" (sem diferenciar maiúsculas e minúsculas)
comeca_com_santo = cidade.upper().startswith("SANTO")

print(f"A cidade começa com 'SANTO'? {comeca_com_santo}")


print('==='*50)
print('--> Versão Guanabarra:')
cid = str(input('Em que cidade você nasceu?')).strip()
print(cid[:5].upper() == 'SANTO')
# print('2ªOpção:')


print('==='*50)
print('The End.')