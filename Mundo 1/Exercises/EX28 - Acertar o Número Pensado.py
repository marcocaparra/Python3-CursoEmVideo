# EX28 - Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
# ----------------------------------------------------------
print('======== EXERCÍCIO 28 ========')

import time
import random

print("Olá, jogador(a), estou pensando em um número de 0 a 5...")
num = random.randint(0, 5)
time.sleep(2)

usuario = int(input(f"Acabei de pensar! Qual você acha que é? "))
if usuario == num:
    print('Parabéns! Você acertou o número que eu tinha pensado.')
else:
    print('Você errou... melhore!')