# EX13 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
# ----------------------------------------------------------
print('======== EXERCÍCIO 13 ========')

salario = float(input("Digite aqui o salário do seu funcionário, e veja o quanto ele irá ganhar com 15% de aumento: R$"))
novo_salario = salario*(5/100)
print(f"O novo salário do funcionário será R${salario+novo_salario}!")