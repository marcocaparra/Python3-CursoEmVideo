# EX67 - Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
# ----------------------------------------------------------
print('======== EXERCÍCIO 67 ========')

while True:
    num = (int(input("Digite um número para ver sua tabuada até x10: ")))
    print('-'*20)
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c} = {num * c}')
        print('-' * 20)
print('FIM DO PROGRAMA... você digitou um número negativo!')