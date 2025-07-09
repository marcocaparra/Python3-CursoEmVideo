# EX49 - Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
# ----------------------------------------------------------
print('======== EXERCÍCIO 49 ========')

num = (int(input("Digite um número para ver sua tabuada até x10: ")))
for c in range(1, 11):
    print(f'{num} x {c} = {num * c}')