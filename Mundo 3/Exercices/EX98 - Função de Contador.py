# EX98 - Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criadas
# ----------------------------------------------------------
print('======== EXERCÍCIO 98 ========')

from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 30)
    print(f'Contagem de {i} até {f}, de {p} em {p}!')
    sleep(2)
    
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}... ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM')
        print('-=' * 30)
    else:
        cont = i
        while cont >= f:
            print(f'{cont}... ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM')
        print('-=' * 30)
    
contador(1, 10, 1)
contador(10, 0, 2)
print('AGORA É SUA VEZ DE PERSONALIZAR A CONTAGEM: ')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)