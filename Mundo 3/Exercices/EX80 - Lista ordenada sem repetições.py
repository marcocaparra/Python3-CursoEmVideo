# EX80 - Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
print('======== EXERCÍCIO 80 ========')

listanum = []
for c in range(0, 5):
    n = int(input('Digite aqui um valor inteiro qualquer: '))
    if c == 0 or c > listanum[-1]:
        listanum.append(n)
        print('Valor adicionado ao final da lista...')
        print('-=' * 30)
    else:
        pos = 0
        while pos < len(listanum):
            if n <= listanum[pos]:
                listanum.insert(pos, n)
                print(f'Valor adicionado a posição {pos} da lista...')
                print('-=' * 30)
                break
            pos += 1
print(f'Você digitou os valores (em ordem): {listanum}')