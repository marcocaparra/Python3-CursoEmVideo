# CL04 - Primeiros comandos em Python3.
# ----------------------------------------------------------
print('======== AULA 4 - Primeiros comandos em Python3 ========')

#Tipos de print:
print('Olá, Mundo!')  # Exibe uma mensagem na tela
print(7+4)  # Exibe o resultado da soma de 7 e 4
print('7'+'4')  # Exibe a string "7+4" sem calcular
print('Olá!', 5) # Exibe a string "Olá!" e o número 5

#Variáveis:
nome = 'Marco'  # Cria uma variável chamada nome e atribui o valor "Marco"
idade = 16  # Cria uma variável chamada idade e atribui o valor 16
print(f'Olá, {nome}! Você tem {idade} anos.')  # Exibe uma mensagem formatada com as variáveis nome e idade

#Input:
nome_usuario = input('Digite seu nome: ')  # Lê o nome do usuário a partir da entrada padrão
idade_usuario = input('Digite sua idade: ')  # Lê a idade do usuário a partir da entrada padrão
peso_usuario = input('Digite seu peso: ')  # Lê o peso do usuário a partir da entrada padrão
print(f'Olá, {nome_usuario}! Você tem {idade_usuario} anos, e pesa {peso_usuario}. Bem-vindo(a) ao Python!")  # Exibe uma mensagem de boas-vindas com o nome do usuário')