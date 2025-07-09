# EX15 - Escreva um programa que pergunta a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
# ----------------------------------------------------------
print('======== EXERCÍCIO 15 ========')

km = float(input("Digite aqui a quantidade de Km percorrido pelo carro que você alugou, para calcular o preço a pagar: "))
dias = int(input("Certo. Agora digite aqui a quantidade de dias alugados: "))
preco = (km * 0.15) + (dias * 60)
print(f"Perfeito! Considerando que você rodou {km}Km, e alugou o carro por {dias} dia(s), o preço a pagar será R${preco}!")