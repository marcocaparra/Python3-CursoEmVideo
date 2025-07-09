# EX52 - Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
# ----------------------------------------------------------
print('======== EXERCÍCIO 52 ========')

num = int(input('Digite aqui um número inteiro: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[mO número {num} foi divisível {tot} vezes!')
if tot == 2:
    print('E por isso ele É primo!')
else:
    print('E por isso ele NÃO É primo!')