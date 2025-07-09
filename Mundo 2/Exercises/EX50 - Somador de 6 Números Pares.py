# EX50 - Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
# ----------------------------------------------------------
print('======== EXERCÍCIO 50 ========')

soma = 0
cont = 0

for c in range(1, 7):
    n = int(input(f'Digite aqui o {c}º número, onde o programa irá fazer a soma apenas dos números pares: '))
    if n % 2 == 0:
        soma = soma + n
        cont = cont + 1
print(f'Você informou {cont} números, e a soma de seus números pares é: {soma}')