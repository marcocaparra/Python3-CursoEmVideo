# EX93 - Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
# ----------------------------------------------------------
print('======== EXERCÍCIO 93 ========')

print('====== BOAS-VINDAS A PLATAFORMA DA "FALA AÍ, JOGADÔ" ======')

from operator import itemgetter

data = {}
partidas = []

data['Nome do Jogador'] = str(input('Digite aqui o nome do jogador: '))
tot = int(input(f'Quantas partidas {data["Nome do Jogador"]} jogou no seu melhor campeonato? '))

print('-' * 30)

for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols {data["Nome do Jogador"]} fez na {c+1} partida desse campeonato? ')))

data['Gols'] = partidas[:]
data['Total de Gols'] = sum(partidas)

print('-=' * 30)

print(data)

print('-=' * 30)

for k, v in data.items():
    print(f'O campo "{k}" possui o valor {v}.')

print('-=' * 30)

print(f'O jogador {data["Nome do Jogador"]} jogou {tot} partida(s).')
for i, v in enumerate(data['Gols']):
        print(f'Na partida {i+1}, {data["Nome do Jogador"]} fez {v} gols.')
