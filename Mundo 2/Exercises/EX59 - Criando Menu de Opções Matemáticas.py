# EX59 - Crie um programa que leia dois valores e mostre um menu na tela.
# ----------------------------------------------------------
print('======== EXERCÍCIO 59 ========')

import time

nome = str(input('Olá, pequeno(a) gafanhoto(a)! Qual é seu nome? ')).strip()
print('-' * 80)
print(f"""Prazer em te conhecer {nome}! Esse é o "Menu Matemático",
feito por Marco Caparra! Vamos lá?""")
print('-' * 80)
time.sleep(1.5)

num1 = int(input('Digite aqui o primeiro número (INTEIRO) para testarmos a plataforma: '))
num2 = int(input('Perfeito! Agora digite aqui o segundo número (INTEIRO): '))
print('-' * 80)
time.sleep(2)
print("""Certo! Esse aqui é seu menu de opções (fique a
vontade para explorar):""")
time.sleep(1.5)
print('-' * 80)
print("""MENU DE OPÇÕES
[ 1 ] - Somar os dois números
[ 2 ] - Multiplicar os dois números
[ 3 ] - Descobrir qual é o maior número
[ 4 ] - Digitar dois novos números
[ 5 ] - Fechar o programa""")
print('-' * 80)
time.sleep(2)

fechar = False
while not fechar:
    usuario = int(input('Qual é sua opção: '))
    if usuario == 1:
        print('-' * 80)
        print(f'A soma entre o números {num1:} e {num2} é: {num1 + num2}!')
        print('-' * 80)
        time.sleep(3)
        print("""MENU DE OPÇÕES
[ 1 ] - Somar os dois números
[ 2 ] - Multiplicar os dois números
[ 3 ] - Descobrir qual é o maior número
[ 4 ] - Digitar dois novos números
[ 5 ] - Fechar o programa""")
        print('-' * 80)

    if usuario == 2:
        print('-' * 80)
        print(f'A multiplicação entre o números {num1:} e {num2:} é: {num1 * num2:}')
        print('-' * 80)
        time.sleep(3)
        print("""MENU DE OPÇÕES
[ 1 ] - Somar os dois números
[ 2 ] - Multiplicar os dois números
[ 3 ] - Descobrir qual é o maior número
[ 4 ] - Digitar dois novos números
[ 5 ] - Fechar o programa""")
        print('-' * 80)

    if usuario == 3:
        if num1 < num2:
            print('-' * 80)
            print(f'O maior número entre {num1} e {num2} é: {num2}')
            print('-' * 80)
        if num1 > num2:
            print('-' * 80)
            print(f'O maior número entre {num1} e {num2} é: {num1}')
            print('-' * 80)
        if num1 == num2:
            print('-' * 80)
            print(f'Os números {num1} e {num2} são iguais. Portanto, não tem um maior!')
            print('-' * 80)
        time.sleep(3)
        print("""MENU DE OPÇÕES
[ 1 ] - Somar os dois números
[ 2 ] - Multiplicar os dois números
[ 3 ] - Descobrir qual é o maior número
[ 4 ] - Digitar dois novos números
[ 5 ] - Fechar o programa""")
        print('-' * 80)

    if usuario == 4:
        num1 = int(input('Digite aqui o novo primeiro número (AINDA INTEIRO): '))
        num2 = int(input('Show! Agora digite aqui o novo segundo número (INTEIRO): '))
        print('...')
        time.sleep(1.5)
        print('Novos números computados!')
        print('-' * 80)
        time.sleep(3)
        print("""MENU DE OPÇÕES
[ 1 ] - Somar os dois números
[ 2 ] - Multiplicar os dois números
[ 3 ] - Descobrir qual é o maior número
[ 4 ] - Digitar dois novos números
[ 5 ] - Fechar o programa""")
        print('-' * 80)

    if usuario == 5:
        fechar = True
        print(f'Obrigador por usar o "Menu Matemático", {nome}!')