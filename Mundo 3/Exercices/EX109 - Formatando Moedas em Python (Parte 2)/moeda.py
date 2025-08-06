# Módulo que será usado para o EX107

def aumentar(num = 0, taxa = 0, form = False):
    res = num + (num * taxa / 100)
    return res if form is False else moeda(res)

def diminuir(num = 0, taxa = 0, form = False):
    res = num - (num * taxa / 100)
    return res if form is False else moeda(res)

def dobro(num = 0, form = False):
    res = num * 2
    return res if not form else moeda(res)

def metade(num = 0, form = False):
    res = num / 2
    return res if not form else moeda(res)

def moeda(num = 0, moeda = 'R$'):
    return f'{moeda}{num:.2f}'.replace('.', ',')