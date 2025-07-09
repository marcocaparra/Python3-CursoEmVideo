# EX45 - Crie um programa que faça o computador jogar Jokenpô com você.
# ----------------------------------------------------------
print('======== EXERCÍCIO 45 ========')

import random
import time

computador = random.randint(0, 2)
itens = ('Pedra', 'Papel', 'Tesoura')
print("""Olá, pequeno(a) gafanhoto(a)! Vamos jogar Jokenpô.
[ 0 ] - Pedra
[ 1 ] - Papel
[ 2 ] - Tesoura""")
jogador = int(input('Qual é sua escolha? '))

print('-'*20)

print('JO')
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('PÔ!')

print(f'Eu escolhi {itens[computador]}...')
print(f'Você escolheu {itens[jogador]}...')

print('-'*20)

if computador == 0:
    if jogador == 0:
        print('EMPATAMOS, VOCÊ ATÉ QUE NÃO É RUIM!')
    elif jogador == 1:
        print('Droga... VOCÊ GANHOU!')
    elif jogador == 2:
        print('VOCÊ PERDEU! AHAHHAHAHAHAHAHHAH')
    else:
        print('Você não escolheu nenhuma das opções... Reinicie o programa e tente novamente!')
elif computador == 1:
    if jogador == 0:
        print('VOCÊ PERDEU! AHAHHAHAHAHAHAHHAH')
    elif jogador == 1:
        print('EMPATAMOS, VOCÊ ATÉ QUE NÃO É RUIM!')
    elif jogador == 2:
        print('Droga... VOCÊ GANHOU!')
    else:
        print('Você não escolheu nenhuma das opções... Reinicie o programa e tente novamente!')
elif computador == 2:
    if jogador == 0:
        print('Droga... VOCÊ GANHOU!')
    elif jogador == 1:
        print('VOCÊ PERDEU! AHAHHAHAHAHAHAHHAH')
    elif jogador == 2:
        print('EMPATAMOS, VOCÊ ATÉ QUE NÃO É RUIM!')
    else:
        print('Você não escolheu nenhuma das opções... Reinicie o programa e tente novamente!')