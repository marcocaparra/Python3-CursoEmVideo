# Módulo que será usado para o EX107, EX108 e EX109

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

def resumo(num = 0, aument = 0, dimin = 0):
    print('-' * 50)
    print('RESUMO DO VALOR'.center(50))
    print('-' * 50)
    print(f'Preço analisado: \t{moeda(num)}')
    print(f'Dobro do preço: \t{dobro(num, True)}')
    print(f'Metade do preço: \t{metade(num, True)}')
    print(f'{aument}% de aumento: \t{aumentar(num, aument, True)}')
    print(f'{dimin}% de redução: \t\t{diminuir(num, dimin, True)}')
        