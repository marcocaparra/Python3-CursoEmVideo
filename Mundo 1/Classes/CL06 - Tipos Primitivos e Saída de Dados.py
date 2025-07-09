# CL06 - Tipos Primitivos e Saída de Dados.
# ----------------------------------------------------------
print('======== AULA 6 - Tipos Primitivos e Saída de Dados ========')

# Tipos primitivos em Python:
# int: número inteiro -> 7, -4, 0, 1000
# float: número real -> 7.0, -4.5, 0.0, 1000.0
# bool: verdadeiro ou falso -> True, False (inicial sempre com letra maiúscula)
# str: cadeia de caracteres -> 'Python', "Curso", '123', "
# print(f"Olá, {'Python'}!") -> Usando o f-string para colocar uma variável dentro de uma string

# Como identificar o tipo de uma variável:
print(type(7))  # Exibe o tipo da variável 7 (int)

# Exemplo do uso do tipo primitivo int:
n1 = int(input('Digite um número para ser somado: '))  # Lê um número inteiro do usuário
n2 = int(input('Digite outro número para ser somado: '))  # Lê outro número inteiro do usuário
soma = n1 + n2  # Calcula a soma dos dois números
print(f'A soma de {n1} e {n2} é igual a {soma}.')  # Exibe o resultado da soma formatado com f-string

# Usando a bilbioteca "is..." para identificar o tipo de uma variável:
carac = input('Digite algo: ')  # Lê uma entrada do usuário
print(carac.isnumeric())  # Verifica se a entrada é numérica
print(carac.isalpha())  # Verifica se a entrada contém apenas letras
print(carac.isalnum())  # Verifica se a entrada contém apenas letras e números
print(carac.isupper())  # Verifica se a entrada está em letras maiúsculas
print(carac.islower())  # Verifica se a entrada está em letras minúsculas
print(carac.isspace())  # Verifica se a entrada contém apenas espaços em branco
