# EX18 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor de seno, cosseno e tangente.
# ----------------------------------------------------------
print('======== EXERCÍCIO 18 ========')

import math
num = float(input("Digite aqui o seu ângulo para ver o seu valor em seno, cosseno e tangente: "))
sen = math.sin(num)
cos = math.cos(num)
tang = math.tan(num)
print(f"Considerando o seu ângulo de {num} graus, seu seno é {math.ceil(sen)}, cosseno é {math.ceil(cos)}, e sua tangente é {math.ceil(tang)}!")