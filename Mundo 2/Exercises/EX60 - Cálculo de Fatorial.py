# EX60 - Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# ----------------------------------------------------------
print('======== EXERCÍCIO 60 ========')

n = int(input('Digite aqui um número para ver seu fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ', end = '')
while c > 0:
    print(f'{c}', end = '')
    if c > 1:
        print(' X ', end = '')
    else:
        print(' = ', end = '')
    f = f * c
    c = c - 1
print(f"{f}")