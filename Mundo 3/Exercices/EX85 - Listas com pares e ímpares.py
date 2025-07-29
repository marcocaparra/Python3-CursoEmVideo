# EX85 - Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
# ----------------------------------------------------------
print('======== EXERCÍCIO 85 ========')

listanum = [[], []]
num = 0
for c in range(1, 8):
    num = int(input(f'Digite aqui o {c}º valor: '))
    if num % 2 == 0:
        listanum[0].append(num)
    else:
        listanum[1].append(num)
print(f'Os valores pares digitados (EM ORDEM CRESCENTE) foram: {sorted(listanum[0])}')
print(f'Os valores ímpares digitados (EM ORDEM CRESCENTE) foram: {sorted(listanum[1])}')