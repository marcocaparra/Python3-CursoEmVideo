# EX95 - Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
# ----------------------------------------------------------
print('======== EXERCÍCIO 95 ========')

print('====== BOAS-VINDAS A PLATAFORMA DA "FALA AÍ, JOGADÔ" ======')

from operator import itemgetter

time = []
data = {}
partidas = []

while True:
    data.clear()
    data['Nome do Jogador'] = str(input('Digite aqui o nome do jogador: '))
    tot = int(input(f'Quantas partidas {data["Nome do Jogador"]} jogou no seu melhor campeonato? '))

    print('-' * 30)

    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols {data["Nome do Jogador"]} fez na {c+1} partida desse campeonato? ')))
    data['Gols'] = partidas[:]
    data['Total de Gols'] = sum(partidas)
    time.append(data.copy())

    while True:
        resp = str(input('Quer continuar [S/N]? ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite apenas S ou N...')
    if resp == 'N':
        break

print('-=' * 30)
print('COD.', end='')
for i in data.keys():
    print(f'{i:<15} ', end='  ')
print()
print('-=' * 30)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 30)

while True:
    mostrar = int(input('Mostrar dados de qual jogador em específico [999 para não buscar nada]? '))
    if mostrar == 999:
        break
    if mostrar >= len(time):
        print(f'ERRO! Não existe jogador com o código {mostrar}...')
    else:
        print('-=' * 30)
        print(f'====== LEVANTAMENTO DO JOGADOR: {time[mostrar]['Nome do Jogador']} ======')
        for i, g in enumerate(time[mostrar]['Gols']):
            print(f'No jogo {i+1}, fez {g} gols!')
print('-=' * 30)
print('====== VOLTE SEMPRE, JOGADÔ! ======')