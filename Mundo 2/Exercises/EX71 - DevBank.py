# EX71 - Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# ----------------------------------------------------------
print('======== EXERCÍCIO 71 ========')

import time

print('-' * 40)
print(f'----------------- DevBank -----------------')
print('-' * 40)

valor = int(input('Olá, usuário(a)! Digite aqui quantos reais você quer sacar? R$'))
total = valor
ced = 50
totalced = 0
print('-' * 40)
print('Carregando...')
time.sleep(2)
print('-' * 40)


while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('-' * 40)
print(f'Volte sempre ao DevBank! Tenha um bom dia.')
print('-' * 40)