# EX73 - Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
# ----------------------------------------------------------
print('======== EXERCÍCIO 73 ========')

tabela_2017 = ('Corinthians', 'Santos', 'Grêmio', 'Palmeiras', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético-MG', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport', 'Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')

print(f'Os 20 primeiros colocados do Campeonato Brasileiro de Futebol são: {tabela_2017}')
print('-'*80)
print(f'Os 5 primeiros colocados são: {tabela_2017[:5]}')
print('-'*80)
print(f'Os 4 últimos colocados são: {tabela_2017[-4:]}')
print('-'*80)
print(f'Os times em ordem alfabética são: {sorted(tabela_2017)}')
print('-'*80)
print(f'O Chapecoense está na {tabela_2017.index("Chapecoense") + 1}ª posição.')