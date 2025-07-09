# EX40 - Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida: Média abaixo de 5.0: REPROVADO. Média entre 5.0 e 6.9: RECUPERAÇÃO. Média 7.0 ou superior: APROVADO.
# ----------------------------------------------------------
print('======== EXERCÍCIO 40 ========')

nota1 = float(input('Olá, aluno(a)! Digite aqui sua primeira nota, afim de calcular sua média: '))
nota2 = float(input('Perfeito! Agora digite aqui a sua segunda nota: '))
media = (nota1 + nota2) / 2
print(f'Considerando sua primeira nota ({nota1:.1f}), e sua segunda nota ({nota2:.1f}), sua média é {media:.1f}!')
if media < 5.0:
    print('Sua média está abaixo de 5.0: REPROVADO')
elif media >= 5.0 and media <= 6.9:
    print('Sua média está ENTRE 5.0 e 6.9: RECUPERAÇÃO')
if media >= 7.0:
    print('Sua média está acima de 7.0: APROVADO')