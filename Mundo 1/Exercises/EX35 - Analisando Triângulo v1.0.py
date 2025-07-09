# EX35 - Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
# ----------------------------------------------------------
print('======== EXERCÍCIO 35 ========')

from time import sleep

print('-='*20)
print('Analisador de Triângulos, iniciando...')
sleep(2)
r1 = float(input('Digite aqui o primeiro segmento do triângulo: '))
r2 = float(input('Digite aqui o segundo segmento do triângulo: '))
r3 = float(input('Digite aqui o terceiro segmento do triângulo: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM formar um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo!')