# CL18 - Listas (Parte 2).
# ----------------------------------------------------------
print('======== AULA 18 - Listas (Parte 2) ========')

dados = list()
dados.append('Gustavo')
dados.append(40)
dados.append('Maria')
dados.append(30)
print(dados)
print(f'O {dados[0]} tem {dados[1]} anos.')

pessoas = list()
pessoas.append(dados[:])  # Adiciona uma cópia de 'dados' na lista 'pessoas'
print(f"Pessoas: {pessoas}")

# Ou

pessoas = [['Gustavo', 40], ['Maria', 30]]
print(pessoas[0][0])  # Acessa o nome de Gustavo
print(pessoas[1][1])  # Acessa a idade de Maria
print(pessoas[0])  # Acessa a lista de Gustavo
print(pessoas[1])  # Acessa a lista de Maria

print('======== PARTE PRÁTICA ========')

teste = list()
teste.append('Gustavo')
teste.append(40)

galera = list()
galera.append(teste[:])  # Adiciona uma cópia de 'teste'

teste[0] = 'Maria'  # Modifica o nome em 'teste'
teste[1] = 30  # Modifica a idade em 'teste'
galera.append(teste[:])  # Adiciona a nova cópia de 'teste'
print(galera)

galera = [['Gustavo', 40], ['Maria', 30]]
print(galera[0][0])  # Acessa o nome de Gustavo
print(galera[1][1])  # Acessa a idade de Maria
print(galera[0])  # Acessa a lista de Gustavo
print(galera[1])  # Acessa a lista de Maria
for p in galera:
    print(f'{p[0]} tem {p[1]} anos.')

galera = []
dado = []
for c in range(3):
    dado.append(input('Nome: '))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()  # Limpa a lista 'dado' para a próxima iteração

totmai = totmen = 0
for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')
    