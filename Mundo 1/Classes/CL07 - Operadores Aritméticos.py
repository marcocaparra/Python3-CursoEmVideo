# CL07 - Operadores Aritméticos.
# ----------------------------------------------------------
print('======== AULA 7 - Operadores Aritméticos ========')

# Operadores aritméticos em Python:
# + : adição
# - : subtração
# * : multiplicação
# / : divisão (retorna float)
# // : divisão inteira (retorna int)
# ** : exponenciação
# % : módulo (resto da divisão)
# == : igualdade
# **(1/2) : raiz quadrada
5 + 2 == 7  # Verifica se 5 + 2 é igual a 7 (retorna True)
5 - 2 == 3  # Verifica se 5 - 2 é igual a 3 (retorna True)
5 * 2 == 10  # Verifica se 5 * 2 é igual a 10 (retorna True)
5 / 2 == 2.5  # Verifica se 5 dividido por 2 é igual a 2.5 (retorna True)
5 // 2 == 2  # Verifica se a divisão inteira de 5 por
5 ** 2 == 25  # Verifica se 5 elevado a 2 é igual a 25 (retorna True)
5 % 2 == 1  # Verifica se o resto da divisão de 5 por 2 é igual a 1 (retorna True)
81 ** (1/2) == 9 # Verifica se a raiz quadrada de 81 é 9 (retorna True)

#Ordem de precedência dos operadores:
# 1. Parênteses ()
# 2. Exponenciação (**)
# 3. Multiplicação (*), Divisão (/), Divisão Inteira (//), Módulo (%) -> O primeiro a ser avaliado é o que aparece primeiro na expressão
# 4. Adição (+), Subtração (-)

#Exemplo do uso de operadores aritméticos no input/print:
nome = input('Digite seu nome: ')
print(f"Prazer em te conhecer, {nome:20}!") # O :20 alinha o nome à direita com 20 espaços
print(f"Prazer em te conhecer, {nome:<20}!") # O :<20 alinha o nome à esquerda com 20 espaços
print(f"Prazer em te conhecer, {nome:>20}!") # O :<20 alinha o nome à direita com 20 espaços
print(f"Prazer em te conhecer, {nome:^20}!") # O :^20 alinha o nome ao centro com 20 espaços
print(f"Prazer em te conhecer, {nome:=^20}!") # O :=^20 alinha o nome ao centro com 20 espaços e preenche com '='

#Exemplo de uso de operadores aritméticos com números:
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
soma = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2
div_int = num1 // num2
expo = num1 ** num2
mod = num1 % num2
print(f'A soma de {num1} e {num2} é igual a {soma}.')
print(f'A subtração de {num1} e {num2} é igual a {sub}.')
print(f'A multiplicação de {num1} e {num2} é igual a {mult}.')
print(f'A divisão de {num1} entre {num2} é igual a {div:.2f}.')  # :.2f formata o resultado para 2 casas decimais
print(f'A divisão inteira de {num1} entre {num2} é igual a {div_int}.')
print(f'A exponenciação de {num1} entre {num2} é igual a {expo}.')
print(f'O módulo de {num1} entre {num2} é igual a {mod}.')

