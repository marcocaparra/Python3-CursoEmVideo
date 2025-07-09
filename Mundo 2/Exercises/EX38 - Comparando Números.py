# EX38 - Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem: O primeiro valor é maior. O segundo valor é maior. Não existe valor maior, os dois são iguais.
# ----------------------------------------------------------
print('======== EXERCÍCIO 38 ========')

num1 = int(input('Digite aqui um número para comparação: '))
num2 = int(input('Digte aqui um segundo número para comparar com o primeiro: '))
if num1 > num2:
    print(f'O maior número é o {num1}, o menor é o {num2}!')
elif num1 < num2:
    print(f'O maior número é o {num2}, o menor é o {num1}!')
elif num1 == num2:
    print('Não existe valor maior, os dois são iguais!')
print('Obrigado por usar nosso comparador :)')