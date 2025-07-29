# EX89 -  Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
# ----------------------------------------------------------
print('======== EXERCÍCIO 89 ========')

ficha = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input(('Deseja continuar? [S/N] ')))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{'Id.':<4}{'NOME':<10}{'MÉDIA':>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:8.1f}')
    print('-' * 26)
mostrar = str(input('Deseja mostrar as notas de algum aluno(a) específico? [S/N] '))
while True:
    if mostrar in 'Nn':
        break
    else:
        aluno = int(input('Deseja ver a nota de qual aluno PELO SEU ID? (-1 para cancelar) '))
        if aluno == -1:
            break
        elif aluno <= len(ficha) - 1:
            print(f'As notas de {ficha[aluno][0]} são: {ficha[aluno][1]}')