# EX32 - Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
# ----------------------------------------------------------
print('======== EXERCÍCIO 32 ========')

from datetime import date

year = int(input('Que ano quer analisar? Digite "0" se você quer analisar o ano atual: '))
if year == 0:
    year = date.today().year
if year % 3 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'O ano {year} é BISSEXTO!')
else:
    print(f"O ano {year} NÃO é BISSEXTO!")