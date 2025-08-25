# arquivo: moeda.py

def aumentar(preco=0, taxa=0):
    """
    Aumenta o preço em uma porcentagem.
    :param preco: valor original
    :param taxa: percentual de aumento
    :return: novo preço
    """
    return preco + (preco * taxa / 100)


def diminuir(preco=0, taxa=0):
    """
    Diminui o preço em uma porcentagem.
    :param preco: valor original
    :param taxa: percentual de redução
    :return: novo preço
    """
    return preco - (preco * taxa / 100)


def dobro(preco=0):
    """
    Retorna o dobro do preço.
    """
    return preco * 2


def metade(preco=0):
    """
    Retorna a metade do preço.
    """
    return preco / 2
