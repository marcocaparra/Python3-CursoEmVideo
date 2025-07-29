# CL17 - listas (Parte 1).
# ----------------------------------------------------------
print('======== AULA 17 - Listas (Parte 1) ========')

lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
print(lanche)

# A grande diferença entre tuplas e listas é que as listas são mutáveis, ou seja, podem ser alteradas.
lanche[3] = 'sorvete'  # Alterando o valor do índice 3
print(lanche)

# Além disso, podemos adicionar novos elementos à lista.
lanche.append('cookie')  # Adicionando 'cookie' ao final da lista
print(lanche)

# Podemos também inserir um elemento em uma posição específica.
lanche.insert(0, 'hot dog')  # Inserindo 'hot dog' na posição 0
print(lanche)

# Podemos remover elementos da lista.
del lanche[1]  # Removendo o elemento na posição 1
print(lanche)
lanche.pop()  # Remove o último elemento da lista
print(lanche)

lanche.remove('pizza')  # Remove o primeiro elemento com o valor 'pizza'
print(lanche)

# Podemos verificar se um elemento está na lista.
if 'hamburguer' in lanche:
    print('Tem hamburguer na lista!')
else:
    print('Não tem hamburguer na lista!')

# Podemos ordenar a lista.
lanche.sort()  # Ordena a lista em ordem alfabética
print(lanche)

# Podemos reverter a ordem da lista.
lanche.reverse()  # Inverte a ordem dos elementos na lista
print(lanche)

# Podemos fazer uma lista usando range.
valores = list(range(1, 11))  # Cria uma lista com números
print(valores)

# Podemos fazer uma lista com números aleatórios.
import random
valores_aleatorios = random.sample(range(1, 100), 10)
print(valores_aleatorios)

# Podemos decobrir o tamanho da lista.
print(f'Tamanho da lista: {len(lanche)}')  # Mostra o tamanho

print('======== PARTE PRÁTICA ========')

# Vamos fazer um pequeno exercício de análise de dados com listas.

while True:
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    altura = float(input('Digite sua altura (em metros): '))
    dados = [nome, idade, altura]  # Criando uma lista com os dados
    print(f'Dados coletados: {dados}')
    adicionar = input('Deseja adicionar outros dados? (s/n): ').lower()
    deletar = input('Deseja deletar os dados? (s/n): ').lower()
    if deletar == 's':
        del dados
        print('Dados deletados.')
    if adicionar == 's':
        continue
    else:
        print('Dados mantidos.')
        break
print('Coleta de dados finalizada!')

# Outro exemplo simples é:
valores = []
for cont in range(0, 5):
    n = int(input('Digite um número: '))
    valores.append(n)
print('Você digitou os valores:', valores)

# Podemos ordenar os valores digitados.
valores.sort()
print('Valores em ordem crescente:', valores)

# Podemos fazer uma ligação entre duas listas.
a = [2, 3, 4, 5]
b = a
B[2] = 8  # Alterando o valor na lista b
print('Lista A:', a)
print('Lista B:', b)

# E para fazer uma cópia de uma lista, usamos o método copy().
a = [2, 3, 4, 5]
b = a.copy()  # Fazendo uma cópia da lista a
b[2] = 8  # Alterando o valor na lista b
print('Lista A:', a)
print('Lista B:', b)
