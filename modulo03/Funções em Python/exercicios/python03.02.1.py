print('Ex.:02 – Um print especial')
print("""
 Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.  
            Ex:                  
                                                                                                                                                         
       escreva(‘Olá, Mundo!’) Saída:                                                                                                                       
         ~~~~~~~~~                                                                                                                                                        
          Olá, Mundo!                                                                                                                                                       
         ~~~~~~~~~                    
""")
print('=====Exercicios====='*8)
# Exercício Python 02
# Exercício Python 097

def escreva(msg):
    tam = len(msg) + 4
    print("~" * tam)
    print(f"  {msg}")
    print("~" * tam)


# Programa principal
escreva("Olá, Mundo!")
escreva("Curso de Python no YouTube")
escreva("André")

print('---Versão Guanabarra---'*7)
def escreva(msg):
    tam = len(msg) + 4
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)



# Programa Principal:
escreva('Andre Luis Kunert')
escreva('Futuro Dev Full Stack pela EStacio')
escreva('Tecnologo em Analista e Desenvolvedor de Sistemas pela UNIASSELVI')






print('=====Exercicios====='*8)


print('The End')