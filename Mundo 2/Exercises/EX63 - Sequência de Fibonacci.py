# EX63 - Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
# ----------------------------------------------------------
print('======== EXERCÍCIO 63 ========')

print('-' * 20)
print('SEQUÊNCIA DE FIBONACCI')
print('-' * 20)

t1 = 0
t2 = 1
n = int(input('Digite aqui quantos termos você quer ver da sequência: '))
print(f'{t1} -> {t2} -> ', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f'{t3} -> ', end='')
    cont = cont + 1
    t1 = t2
    t2 = t3
print('FIM', end='')
