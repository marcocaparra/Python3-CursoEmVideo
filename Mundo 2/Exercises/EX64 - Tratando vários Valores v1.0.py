# EX64 - Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
# ----------------------------------------------------------
print('======== EXERCÍCIO 64 ========')

n = cont = soma = 0
n = int(input('Digite aqui um número inteiro [999 para parar o programa]: '))
while n != 999:
    soma = soma + n
    cont = cont + 1
    n = int(input('Digite aqui um número inteiro [999 para parar o programa]: '))
print(f'Você digitou {cont} números que somando, resultam em: {soma}')