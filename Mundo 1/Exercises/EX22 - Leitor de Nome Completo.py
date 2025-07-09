# EX22 - Crie um programa que leia o nome completo de uma pessoa e mostre: O nome com todas as letras maiúsculas. O nome com todas minúsculas. Quantas letras ao todo (sem considerar espaços). Quantas letras tem o primeiro nome.
# ----------------------------------------------------------
print('======== EXERCÍCIO 22 ========')

complet_name = str(input("Olá, digite aqui seu nome completo e veja algumas informações sobre ele: ")).strip()
print(f"Show! O nome {complet_name} fica dessa forma com todas letras maíusculas: {complet_name.upper()}")
print(f"O nome {complet_name} fica dessa forma com todas letras minúsculas: {complet_name.lower()}")
print(f"O nome {complet_name} possui {len(complet_name) - complet_name.count(" ")} letras no total!")
print(f"E no seu primeiro nome, possuem {complet_name.find(" ")}!")