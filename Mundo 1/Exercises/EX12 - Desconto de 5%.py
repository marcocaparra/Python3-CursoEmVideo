# EX12 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
# ----------------------------------------------------------
print('======== EXERCÍCIO 12 ========')

preco = float(input("Digite aqui o preço do produto para calcular o valor do mesmo com 5% de desconto: R$"))
desconto = preco*(5/100)
print(f"O preço de R${preco} cai para R${preco-desconto}!")