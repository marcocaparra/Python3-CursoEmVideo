# EX100 - Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
# ----------------------------------------------------------
print('======== EXERCÍCIO 100 ========')

from random import randint
from time import sleep

números = []
pares = []

def sorteia(lista):
    for c in range(0, 5):
        números.append(randint(0, 100))
    print(f'Os valores sorteados foram: ', end='')
    for n in números:
        print(f'{n}... ', end='', flush=True)
        sleep(1)
    print('FIM!')

def somaPar(lista):
    for n in números:
        if n % 2 == 0:
            pares.append(n)
    soma = 0
    for p in pares:
        soma = soma + p
    print(f'A soma entre todos os pares digitados {pares} é: {soma}')

print(f'Sortendo 5 valores para uma lista aleatória...')
sleep(1.5)
sorteia(números)
sleep(1.5)
somaPar(números)