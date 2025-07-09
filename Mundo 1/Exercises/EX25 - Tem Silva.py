# EX25 - Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
# ----------------------------------------------------------
print('======== EXERCÍCIO 25 ========')

import time

nome = str(input("Digite aqui seu nome para verificar uma informação EXTREMAMENTE IMPORTANTE: ")).strip()
nome_up = nome.upper()
print(f"Analisando o nome {nome}...")
time.sleep(2)
print(f"Seu nome tem Silva? {"SILVA" in nome_up}")
