def leiadinherio(msg):
    valido = False
    while not valido:
        entrada = str(input(msg))
        if entrada.isalpha():
            print(f' ERRO:\" {entrada}" é Preço Inválido')
        else:
            valido = True
            return float(entrada)

