# EX30 - Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
# ----------------------------------------------------------
print('======== EXERCÍCIO 30 ========')

usuary_number = int(input('Digite aqui um número inteiro qualquer: '))
result = usuary_number % 2
if result == 0:
    print(f"O número {usuary_number} é PAR!")
else:
    print(f"O número {usuary_number} é ÍMPAR!")
