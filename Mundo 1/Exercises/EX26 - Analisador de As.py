# 26 - Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
# ----------------------------------------------------------
print('======== EXERCÍCIO 26 ========')

nome = str(input("Digite aqui seu nome para ver algumas informações sobre ele: ")).strip()
nome_up = nome.upper()
print(f"A letra A apareceu {nome_up.count("A")} vezes na frase...")
print(f"A primeira letra A aparece na posição {nome_up.find("A")+1}...")
print(f"A última letra A aparece na posição {nome_up.rfind("A")+1}...")