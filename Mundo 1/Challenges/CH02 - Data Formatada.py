# CH02 (Baseado na aula #04 -> Primeiros comandos em Python3) - Crie um script que leia o dia, mês e ano de nascimento do usuário e exiba a data formatada.
# ----------------------------------------------------------
print("======== DESAFIO 2 ========")
nome = input("Olá, usuário! Qual é o seu nome? ")  # Lê o nome do usuário
dia =  input(f"Certo, {nome}! Qual é o dia do seu nascimento? ")  # Lê o dia de nascimento do usuário
mes = input(f"Qual é o mês do seu nascimento? ")  # Lê o mês de nascimento do usuário
ano = input(f"Por fim, qual é o ano do seu nascimento? ")  # Lê o ano de nascimento do usuário
print(f"{nome}, então você nasceu no {dia} do {mes} de {ano}!")  # Exibe a data formatada