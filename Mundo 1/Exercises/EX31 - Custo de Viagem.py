# EX31 - Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
# ----------------------------------------------------------
print('======== EXERCÍCIO 31 ========')

distance = float(input("Digite aqui a distância da viagem, em Km: "))
if distance <= 200:
    price = distance * 0.50
else:
    price = distance * 0.45
print(f"O preço da passagem será R${price}!")