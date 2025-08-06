# EX101 - Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
# ----------------------------------------------------------
print('======== EXERCÍCIO 101 ========')

def voto(ano=0):
    from datetime import datetime
    atual = datetime.now().year
    result = atual - ano
    if result < 16:
        return f'Com {result} anos você NÃO VOTA!'
    elif 16 < result < 18 or result > 65:
        return f'Com {result} anos o VOTO É OPCIONAL!'
    else:
        return f'Com {result} anos o VOTO É OBRIGATÓRIO!'
    
idade = int(input('Em qual ano você nasceu? '))
print(voto(idade))