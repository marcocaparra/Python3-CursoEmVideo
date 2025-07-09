# EX57 - Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
# ----------------------------------------------------------
print('======== EXERCÍCIO 57 ========')

sexo = str(input("""Informe aqui seu sexo! Se for masculino, digite "M",
se for feminino, digite "F": """)).upper().strip()
while sexo not in 'MmFf':
    sexo = str(input('Você não digitou nem "M", nem "F"... Tente novamente: ')).upper().strip()
    if sexo == 'M':
        print('Seja bem VINDO!')

    if sexo == 'F':
        print('Seja bem VINDA!')
print('Obrigado por usar nosso site!')
