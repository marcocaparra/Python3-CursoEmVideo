# EX33 - Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
# ----------------------------------------------------------
print('======== EXERCÍCIO 33 ========')

num1 = int(input("Digite aqui um número: "))
num2 = int(input("Digite aqui outro número: "))
num3 = int(input("Digite aqui um último número: "))
if num1 < num2 and num1 < num3:
    menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
if num1 > num2 and num1 > num3:
    maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
print(f"O maior número é {maior}, já o menor é {menor}!")
