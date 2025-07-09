# EX03 - Crie um script que leia dois números e tente mostrar a soma entre eles.
# ----------------------------------------------------------
print('======== EXERCÍCIO 3 ========')

num1 = int(input('Digite o primeiro número que será somado: ')) # Por causa do int, ele detecta que o valor digitado é um inteiro (número)
num2 = int(input('Digite o segundo número que será somado: '))
soma = num1 + num2
print(f'A soma entre os dois números que você escolheu para serem somados, é: {soma}')