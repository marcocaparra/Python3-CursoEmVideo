# EX65 - Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
# ----------------------------------------------------------
print('======== EXERCÍCIO 65 ========')

resp = 'S'
soma = quant = media = maior = menor = 0
while resp == 'S':
    n = int(input('Digite aqui um número INTEIRO: '))
    soma = soma + n
    quant = quant + 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Você quer continuar [S/N]? ')).strip().upper()[0]
media = soma / quant
print(f"""Você digitou {quant} números, e a média entre eles é {media:.2f}!
Além disso, o maior número foi {maior}, e o menor foi {menor}.""")