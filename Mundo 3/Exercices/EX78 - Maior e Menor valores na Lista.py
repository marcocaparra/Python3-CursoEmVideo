# EX78 - Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
# ----------------------------------------------------------
print('======== EXERCÍCIO 78 ========')
    
listanum = []
for c in range(0, 5):
    listanum.append(int(input(f'Digite aqui um valor para a posição {c}: ')))

maior = max(listanum)
menor = min(listanum)
print('-=' * 30)
print(f'Você digitou os seguintes valores: {listanum}')
print(f'O primeiro maior valor que você digitou foi {maior}. Esse valor foi encontrado na posição {listanum.index(maior)}')
print(f'O primeiro menor valor que você digitou foi: {menor}. Esse valor foi encontrado na posição {listanum.index(menor)}')