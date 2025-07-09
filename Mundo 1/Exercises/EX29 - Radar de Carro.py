# EX29 - Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
# ----------------------------------------------------------
print('======== EXERCÍCIO 29 ========')

veloc = float(input('Qual é a velocidade atual do carro? '))
if veloc > 80.0:
    excesso = veloc - 80.0
    multa = excesso * 7
    print(f'Você ultrapassou a velocidade de 80Km/h irá ter que pagar uma multa de R${multa:.2f}!')
else:
    print('Tudo certo!')
print('Tenha um bom dia! Dirija com segurança.')