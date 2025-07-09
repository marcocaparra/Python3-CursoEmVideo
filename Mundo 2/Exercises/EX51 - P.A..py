# EX51 - Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
# ----------------------------------------------------------
print('======== EXERCÍCIO 51 ========')

print('-'*20)
print('DEMONSTRAÇÃO RÁPIDA DE 10 TERMOS DE UMA PROGRESSÃO ARITMÉTICA')
print('-'*20)

termo1 = int(input('Digite aqui o primeiro termo dessa P.A: '))
razao = int(input('Digite aqui a razão dessa P.A: '))
decimo = termo1 + (10 - 1) * razao
for c in range(termo1, decimo + razao, razao):
    print(c, end=' -> ')
print('FIM!')