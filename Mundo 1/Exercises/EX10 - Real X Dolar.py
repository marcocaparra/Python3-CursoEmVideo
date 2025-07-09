# EX10 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira, e mostre quantos dólares ela pode comprar (CONSIDERANDO US$1,00 = R$3,27)
# ----------------------------------------------------------
print('======== EXERCÍCIO 10 ========')

din = float(input("Digite aqui quantos reais você tem na carteira, para saber quantos dólares pode comprar: R$"))
print(f"Com R${din}, você pode comprar U${din/3.27:.2f}!")