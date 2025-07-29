# EX88 -  Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
# ----------------------------------------------------------
print('======== EXERCÍCIO 88 ========')

import random
import time

lista = []
jogos = []
print('-' * 30)
print(      'SORTEIO DA MEGA ROUBA (OPS, SENA)'     )
print('-' * 30)
quant = int(input('Quantos jogos você quer sortear? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        numeros = random.randint(1, 60)
        if numeros not in lista:
            lista.append(numeros)
            cont += 1
        if cont >= 6:
            break
    lista.sort
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-' * 30)
print('-' * 3, f'SORTEANDO {quant} JOGOS...', '-' * 3)
time.sleep(1.5)
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    time.sleep(1)