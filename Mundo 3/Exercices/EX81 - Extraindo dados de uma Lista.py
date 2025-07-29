# EX81 - Crie um programa que vai ler vários números e colocar em uma lista.                  Depois disso, mostre:                                                                                                                                                A) Quantos números foram digitados.                                                                                                                    B) A lista de valores, ordenada de forma decrescente.                                                                                          C) Se o valor 5 foi digitado e está ou não na lista.
print('======== EXERCÍCIO 81 ========')

listanum = []
while True:
    listanum.append(int(input('Digite aqui um valor inteiro qualquer: ')))
    r = str(input('Você deseja continuar? [S/N] ')).strip().lower()
    if r in 'Nn':
        break
print('-=' * 30)
print(f'Você digitou {len(listanum)} elementos.')
listanum.sort(reverse=True)
print(f'Os valores em ordem descrescente são {listanum}.')
if 5 in listanum:
    print('O valor 5 foi encontrado na lista.')
else:
    print('O valor 5 não foi encontrado na lista.')