# CL19 - Dicionários.
# ----------------------------------------------------------
print('======== AULA 19 - Dicionários ========')

# Dicionários são estruturas de dados que armazenam pares de chave-valor.
# Eles são mutáveis e não possuem ordem definida.

filme_starwars = {
    'titulo': 'Star Wars: O Império Contra-Ataca',
    'ano': 1980,
    'diretor': 'Irvin Kershner',
    'elenco': ['Mark Hamill', 'Harrison Ford', 'Carrie Fisher']
}

filme_matrix = {
    'titulo': 'Matrix',
    'ano': 1999,
    'diretor': 'Lana Wachowski, Lilly Wachowski',
    'elenco': ['Keanu Reeves', 'Laurence Fishburne', 'Carrie-Anne Moss']
}

filme_avengers = {
    'titulo': 'Vingadores: Ultimato',
    'ano': 2019,
    'diretor': 'Anthony Russo, Joe Russo',
    'elenco': ['Robert Downey Jr.', 'Chris Evans', 'Scarlett Johansson']
}

print(filme_starwars)
print(filme_starwars['titulo'])
print(filme_starwars.values()) # Retorna todos os valores do dicionário
print(filme_starwars.keys())   # Retorna todas as chaves do dicionário
print(filme_starwars.items())  # Retorna todos os pares chave-valor do dicionário

print('-=-' * 20)

# Podemos usar o "for" para iterar sobre os itens do dicionário.
for chave, valor in filme_starwars.items():
    print(f'{chave}: {valor}')

print('-=-' * 20)

# Podemos juntar listas, tuplas e dicionários.
locadora = [filme_starwars, filme_matrix, filme_avengers]
print(locadora)
print(f'Número de filmes na locadora: {len(locadora)}')
print(locadora[0]['titulo'])  # Acessando o título do primeiro filme
print(locadora[1]['ano'])     # Acessando o ano do segundo filme

print('-=-' * 20)

print('======== PARTE PRÁTICA ========')

pessoas = {'nome': 'Marco', 'sexo': 'M', 'idade': 16}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos!')
# Ou
for k, v in pessoas.items():
    print(f'{k} = {v}')

print('-=-' * 20)

brasil = []
estado1 = {'UF': 'São Paulo', 'Sigla': 'SP'}
estado2 = {'UF': 'Rio de Janeiro', 'Sigla': 'RJ'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0])
print(brasil[0]['UF'])

print('-=-' * 20)

estado = {}
brasil = []
for c in range(3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())  # Usamos copy() para evitar referências
for e in brasil:
    for k, v in e.items():
        print(f'{k} = {v}')