# EX84 - Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
# ----------------------------------------------------------
print('======== EXERCÍCIO 84 ========')

temp = []
princ = []
mai = men = 0
while True:
    nome = temp.append(str(input('Digite um nome: ')))
    peso = temp.append(float(input('Digite o peso desse ser: ')))
    print('Dados cadastrados!')
    print('-=' * 30)
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        elif temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Ao todo, foram cadastrados {len(princ)} seres.')
print(f'Os seres cadastrados com maiores pesos ({mai}) foram: ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}]')
print(f'Os seres cadastrados com menores pesos ({men}) foram: ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}]')
    