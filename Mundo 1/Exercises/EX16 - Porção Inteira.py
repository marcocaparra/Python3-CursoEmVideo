# EX16 - Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
# ----------------------------------------------------------
print('======== EXERCÍCIO 16 ========')

import math
num = float(input("Digite aqui um número para ver sua porção inteira: "))
porc_int = math.trunc(num)
print(f"Considerando que você digitou {num}, sua porção inteira é {porc_int}!")