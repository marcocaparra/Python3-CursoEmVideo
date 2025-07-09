# EX70 - Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não.
# ----------------------------------------------------------
print('======== EXERCÍCIO 70 ========')

print('-' * 20)
print('========= LOJA DO SEU TOBA =========')
print('-' * 20)

total = pcaro = cont = menor = 0

while True:
    produto = str(input('Nome do Produto: ')).strip()
    preco = float(input(f'Certo. Qual é o preço do(a) {produto}? R$'))
    total += preco
    cont += 1
    if preco > 1000:
        pcaro += 1
    if cont == 1 or preco < menor:
        menor = preco
    print('-' * 20)

    resp=' '
    while resp not in 'SNsn':
        resp = str(input('Você quer digitar mais um produto? [S/N] ')).strip().upper()[0]
    if resp in 'Nn':
        break
print('-' * 20)
print('Fim do Programa Seu Toba')
print('-' * 20)
print(f'Você gastou um total de R${total:.2f}')
print(f'Temos {pcaro} produto(s) custando mais de R$1000')
print(f'O produto mais barato custa R${menor:.2f}')