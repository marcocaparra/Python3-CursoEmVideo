# EX07 - Desenvolva um programa que leia as duas notas de um aluno, e calcule sua média.
# ----------------------------------------------------------
print('======== EXERCÍCIO 7 ========')

aluno = str(input("Digite aqui o nome do aluno(a): "))
nota1 = float(input(f"Digite aqui a primeira nota do(a) {aluno} para calcular sua média: "))
nota2 = float(input(f"Digite aqui a segunda nota do(a) {aluno}: "))
print(f"Certo. A média do(a) {aluno}, considerando que suas notas são {nota1} e {nota2}, é {(nota1+nota2)/2}")