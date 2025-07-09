# EX41 - A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# ----------------------------------------------------------
print('======== EXERCÍCIO 41 ========')

import datetime

data = int(input('Olá, atleta! Digite aqui a sua data de nascimento: '))
atual = datetime.date.today().year
idade = atual - data
if 0 < idade <= 9:
    print('Você é um atleta MIRIM!')
elif 10 < idade <= 14:
    print('Você é um atleta INFANTIL!')
elif 15 < idade <= 19:
    print('Você é um atleta JÚNIOR!')
elif 20 < idade <= 25:
    print('Você é um atleta SÊNIOR!')
else:
    print('Você é um atleta MASTER!')
print('Obrigado por usar o programa da Confederação Nacional de Natação!')