# EX36 - Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
# ----------------------------------------------------------
print('======== EXERCÍCIO 36 ========')

casa = float(input("Qual é o valor da casa que você irá comprar? R$"))
salario = float(input("Qual é seu salário atual? R$"))
anos = int(input("Por quantos anos você irá pagar a casa? "))
prestacao = casa / (anos * 12)
minimo = salario * 30/100
print(f"Para pagar uma casa de R${casa}, em {anos} anos, a prestação é de {prestacao:.2f}!")
if prestacao <= minimo:
    print('O empréstimo PODE ser concedido.')
else:
    print('O seu empréstimo foi NEGADO.')
print('Tenha um bom dia!')