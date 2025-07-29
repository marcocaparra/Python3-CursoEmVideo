# EX91 -  Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
# ----------------------------------------------------------
print('======== EXERCÍCIO 91 ========')

from random import randint
from time import sleep
from operator import itemgetter

print('====== BOAS-VINDAS AO SORTEADOR (DADO) DIGITAL ======')

players = {
    'P1': randint(1, 6),
    'P2': randint(1, 6),
    'P3': randint(1, 6),
    'P4': randint(1, 6)
}

ranking = []

for k, v in players.items():
    print(f'O valor sorteado no dado, para o {k} é: {v}')
    sleep(1)

ranking = sorted(players.items(), key=itemgetter(1), reverse=True)

print('-=' * 30)
print('====== RANKING ======')

for i, v in enumerate(ranking):
    print(f'{i+1}º LUGAR: {v[0]} com o número: {v[1]}')

print('-=' * 30)
print('PARABÉNS A TODOS!')