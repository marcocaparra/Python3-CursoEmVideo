# EX82 - Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
print('======== EXERCÍCIO 82 ========')

listanum = []
pares = []
impares = []
while True:
    n = listanum.append(int(input('Digite um valor inteiro qualquer: ')))
    r = str(input('Deseja continuar: [S/N] ')).strip()
    if r in 'Nn':
        break

for i, v in enumerate(listanum):
    if v % 2 == 0:
        pares.append(v)
    elif v % 1 == 0:
        impares.append(v)

print('-=' * 30)
print(f'A lista completa é {listanum}')
print(f'Os valores pares da lista são: {pares}')
print(f'Os valores ímpares da lista são {impares}')