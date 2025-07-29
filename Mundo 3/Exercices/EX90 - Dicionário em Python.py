# EX90 -  Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
# ----------------------------------------------------------
print('======== EXERCÍCIO 90 ========')

dict = {}

dict['Nome'] = str(input('Nome do Aluno: '))
dict['Média'] = float(input(f'Certo. Qual foi a média do {dict["Nome"]}? '))
if dict['Média'] < 6:
    print('Vish...')
else:
    print('Show!')
print('-=' * 30)
print(f'O nome do aluno é {dict["Nome"]}')
print(f'A média de {dict["Nome"]} é: {dict["Média"]}')
if 3 < dict['Média'] < 6:
    print(f'O(a) {dict["Nome"]} está de RECUPERAÇÃO. Ele pode recuperar.')
elif dict['Média'] <= 3:
    print(f'O(a) {dict["Nome"]} está REPROVADO...')
else:
    print(f'O(a) {dict["Nome"]} está APROVADO. PARABÉNS!')