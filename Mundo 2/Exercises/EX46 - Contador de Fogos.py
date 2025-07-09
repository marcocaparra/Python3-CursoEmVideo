# EX46 - Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
# ----------------------------------------------------------
print('======== EXERCÍCIO 46 ========')

from time import sleep

print('Globo: Contagem regressiva de apenas 10 segundos para o Ano Novo e o estouro dos fogos de artifício...')
sleep(1)
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('FELIZ ANO NOVO!!!!!!!!!!!!!!!!')