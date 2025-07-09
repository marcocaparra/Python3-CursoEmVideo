# EX44 -  Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento
# ----------------------------------------------------------
print('======== EXERCÍCIO 44 ========')

preco = float(input('Preço da(s) compra(s): R$'))
print("""Qual será sua forma de pagamento?
[ 1 ] - À vista (com dinheiro o cheque)
[ 2 ] - À vista no cartão
[ 3 ] - 2x no cartão
[ 4 ] - 3x ou mais no cartão""")
escolha = int(input('Qual opção você prefere? '))

if escolha == 1:
    valor = preco - (preco * 10 / 100)
    print(f"""Perfeito! Escolhendo à vista no cartão ou cheque, você ganha 10% de desconto.
Logo, sua compra passa de R${preco:.2f} para R${valor:.2f}!""")
elif escolha == 2:
    valor = preco - (preco * 5 / 100)
    print(f"""Certo. Escolhendo à vista no cartão ou cheque, você ganha 5% de desconto.
Logo, sua compra passa de R${preco:.2f} para R${valor:.2f}!""")
elif escolha == 3:
    total = preco
    parcela = preco / 2
    print(f'Sua compra será parcela em 2x de R${parcela:.2f} SEM JUROS!')

elif escolha == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input('Quantas parcelar? '))
    parcela = total / totparc
    print(f'Sua compra será parcelada em {totparc:.2f} de R${parcela:.2f} COM JUROS!')