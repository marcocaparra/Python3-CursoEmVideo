# EX99 - Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
# ----------------------------------------------------------
print('======== EXERCÍCIO 99 ========')

from time import sleep

def analiseValores(*valores):
    print('-=' * 30)
    print('Analisando os valores passados...')
    sleep(2)
    print(f'{valores}. Foram informados {len(valores)} ao todo.')
    sleep(1.5)
    print(f'O maior valor informado foi {max(valores)}!')
    sleep(1.5)

analiseValores(2, 9, 4, 5, 7, 1)
analiseValores(4, 7, 0)
analiseValores(1, 2)
analiseValores(6)