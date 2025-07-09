# EX23 - Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# ----------------------------------------------------------
print('======== EXERCÍCIO 23 ========')

import time
num = int(input("Digite aqui um número e veja seus dígitos separadamentes por casa decimal: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f"Analisando o número {num}...")
time.sleep(2)
print(f"A unidade do número {num} é {u}!")
print(f"A dezena do número {num} é {d}!")
print(f"A centena do número {num} é {c}!")
print(f"O milhar do número {num} é {m}!")