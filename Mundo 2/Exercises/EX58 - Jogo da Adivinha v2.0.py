# EX58 - Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
# ----------------------------------------------------------
print('======== EXERCÍCIO 58 ========')

import random
import time

computador = random.randint(1, 10)

print("""Olá, pequeno(a) gafanhoto(a)! Você irá tentar adivinhar
um número de 1 a 10 que eu vou pensar. Preparado?""")

time.sleep(4)
print('Estou pensando no número...')
time.sleep(2)
print('PRONTO!')
print('-'*20)

cont = 0
acertou = False
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    cont = cont + 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('-' * 20)
            print('Tente escolher um valor mais alto...')
        elif jogador > computador:
            print('-' * 20)
            print('Tente escolher um valor mais baixo...')
print('-'*20)
print(f'Você GANHOU fazendo {cont} jogada(s). Bom jogo, pequeno(a) gafanhoto(a)!')