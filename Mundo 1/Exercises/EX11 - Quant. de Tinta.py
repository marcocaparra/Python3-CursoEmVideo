# EX11 - Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
# ----------------------------------------------------------
print('======== EXERCÍCIO 11 ========')

larg = float(input("Digite aqui a largura da parede que você quer pintar, em metros: "))
alt = float(input("Digite aqui a altura da parede: "))
area = larg * alt
print(f"A área dessa parede é {area}m²... logo, você precisara de {area/2}L de tinta!")