# EX75 - Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# ----------------------------------------------------------
print('======== EXERCÍCIO 75 ========')

while True:
    n1 = int(input('Digite aqui um primeiro número: '))
    n2 = int(input('Digite aqui um segundo número: '))
    n3 = int(input('Digite aqui um segundo número: '))
    n4 = int(input('Digite aqui um quarto número: '))
    print("-" * 50)
    cont = 4


    n = (n1, n2, n3, n4)

    cont_9 = 0

    if 9 in n:
        cont_9 = n.count(9)
        print(f'O número 9 foi digitado {cont_9} vezes.')
        print("-" * 50)
    
    if 3 in n:
        print(f'O primeiro número 3 apareceu na posição {n.index(3) + 1}.')
        print("-" * 50)
    
    
    for num in n:
        if num % 2 == 0:
            print(f'O valor par digitado foi: {num}.')
            print("-" * 50)

    if 9 not in n and 3 not in n and num % 2 != 0:
        print('Não recebemos valores suficientes para trazermos uma análise do dados...')
        print("-" * 50)

    if cont == 4:
        break
print('Obrigado por usar nosso Analisador de Dados. Tenha um bom dia!')