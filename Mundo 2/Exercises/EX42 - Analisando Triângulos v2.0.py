# EX42 - Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# ----------------------------------------------------------
print('======== EXERCÍCIO 42 ========')

from time import sleep

print('-='*20)
print('Analisador de Triângulos, iniciando...')
sleep(2)
r1 = float(input('Digite aqui o primeiro segmento do triângulo: '))
r2 = float(input('Digite aqui o segundo segmento do triângulo: '))
r3 = float(input('Digite aqui o terceiro segmento do triângulo: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM formar um triângulo ', end=' ')
    if r1 == r2 == r2:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo!')