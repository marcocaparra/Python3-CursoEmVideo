# EX27 - Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# ----------------------------------------------------------
print('======== EXERCÍCIO 27 ========')

nome = str(input("Digite aqui seu nome para ver algumas informaçõe sobre ele: ")).strip()
print(f"Prazer em te conhecer {nome}!")
nome_split = nome.split()
print(f"Seu primeiro nome é {nome_split[0]}!")
print(f"Seu último nome é {nome_split[len(nome_split)-1]}!")
