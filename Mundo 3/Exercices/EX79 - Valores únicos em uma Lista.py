# EX79 - Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
print('======== EXERCÍCIO 79 ========')

listanum = []
while True:
    n = int(input('Digite um valor: '))
    print('-=' * 30)
    if n not in listanum:
        listanum.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Deseja continuar? [S/N] '))
    if r in 'Nn':
        break
print("-=" * 30)
print(f'Você digitou os valores: {sorted(listanum)}')