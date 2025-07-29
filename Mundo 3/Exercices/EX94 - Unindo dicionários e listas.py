# EX94 - Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média.
# ----------------------------------------------------------
print('======== EXERCÍCIO 94 ========')

dados = {}
pessoas = []
soma = media = 0

while True:
    dados.clear()
    dados['Nome'] = str(input('Nome: ')).strip()

    while True:
        dados['Sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if dados['Sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F...')

    dados['Idade'] = int(input('Idade: '))
    soma += dados['Idade']
    pessoas.append(dados.copy())

    while True:
        resp = str(input('Quer continuar [S/N]? ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite apenas S OU N...')
    if resp == 'N':
        break

print('-=' * 30)
print(f'Ao total, foram cadastradas {len(pessoas)} pessoas no sistema.')
media = soma / len(pessoas)
print(f'A média das idades cadastradas é: {media:.0f}')
print('As mulheres cadastradas foram: ', end='')
for pessoa in pessoas:
    if pessoa['Sexo'] == 'F':
        print(f"{pessoa['Nome']}.")
print('As pessoas que estão com a idade acima da média calculada são: ', end='')
for p in pessoas:
    if p['Idade'] > media:
        print(f"{p['Nome']}.")
 