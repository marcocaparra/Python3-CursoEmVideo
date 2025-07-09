# EX17 - Faça um programa que leia o comprimento do cateto oposto e adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
# ----------------------------------------------------------
print('======== EXERCÍCIO 17 ========')

import math
cat_op = float(input("Digite aqui o cateto oposto do seu triângulo retângulo para calcular a hipotenusa: "))
cat_ad = float(input("Digite aqui o cateto adjacente do seu triângulo retângulo para calcular a hipotenusa: "))
hip = math.sqrt((math.pow(cat_op, 2))+ (math.pow(cat_ad, 2)))
print(f"A hipotenusa dos catetos {cat_op} e {cat_ad}, é: {hip:.2f}")