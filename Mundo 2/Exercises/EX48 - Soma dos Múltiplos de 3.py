# EX48 - Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
# ----------------------------------------------------------
print('======== EXERCÍCIO 48 ========')

import time

print("""Olá, usuário(a)! Nesse programa em Python ABSURDAMENTE inovador, você irá ver a soma
de todos os múltiplos de 3, do 1 até 500.""")
time.sleep(1.5)
print('A soma é:')
time.sleep(0.5)
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print(f'A soma dos {cont} valores solicitados é: {soma}')