# EX24 - Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
# ----------------------------------------------------------
print('======== EXERCÍCIO 24 ========')

c = str(input("Digite aqui a cidade que você mora: ")).strip()
c_up = c.upper()
print(f"A sua cidade começa com Santo? {c_up[:5] == "SANTO"}")
