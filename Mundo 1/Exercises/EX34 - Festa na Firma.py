# EX34 - Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
# ----------------------------------------------------------
print('======== EXERCÍCIO 34 ========')

salary = float(input('Digite aqui qual é o salário do funcionário: R$'))
if salary > 1250.00:
    aumento = salary + (salary * 10 / 100)
else:
    aumento = salary + (salary * 15 / 100)
print(f"Considerando o salário anterior de R${salary}, o funcionário passa a ganhar R${aumento}!")
