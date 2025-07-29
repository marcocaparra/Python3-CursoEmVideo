# EX96 - Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
# ----------------------------------------------------------
print('======== EXERCÍCIO 96 ========')

def calculoArea(l, c):
    a = l * c
    print(f'''A área de um terreno triangular, a partir da
altura {l}m e o comprimento {c}m, é: {a}m²!''')

print('-=' * 30)
print('Controle de Terrenos':^30)
print('-=' * 30)
l = float(input('LARGURA do terreno (m): '))
c = float(input('COMPRIMENTO do terreno (m): '))
calculoArea(l, c)