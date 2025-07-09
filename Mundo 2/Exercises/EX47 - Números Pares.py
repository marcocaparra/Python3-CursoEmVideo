# EX47 - Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
# ----------------------------------------------------------
print('======== EXERCÍCIO 47 ========')

import time

print("""Olá, usuário(a)! Nesse programa em Python totalmente inovador, você irá ver
quais são os números pares de 1 até 50.""")
time.sleep(1.5)
print('Os números são: ')
time.sleep(0.5)
for c in range(2, 51, 2):
    print(c)
    time.sleep(1)
print('Tente não chorar com tanta inovação...')