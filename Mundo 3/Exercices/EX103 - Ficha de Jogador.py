# EX103 - Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
# ----------------------------------------------------------
print('======== EXERCÍCIO 103 ========')

def ficha(nome=0, gols=0):
    gols = f'{gols}'
    if nome is None or nome in ' ' or nome.isalpha() == False:
        nome = 'DESCONHECIDO'
    if gols.isnumeric():
        gols = gols
    else:
        gols = 0
    return f'O jogador {nome} fez {gols} gol(s) no campeonato!'

nome = str(input('Nome do Jogador: ')).strip()
gols = str(input('Número de Gols: '))

print(ficha(nome, gols))