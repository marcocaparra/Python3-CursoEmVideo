# EX107 - Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
# ----------------------------------------------------------
print('======== EXERCÍCIO 107 ========')

import moeda

num = float(input('Digite aqui um número aleatório: '))
print(f'A metade de R${num} é R${moeda.metade(num):.2f}')
print(f'O dobro de R${num} é R${moeda.dobro(num):.2f}')
print(f'Adicionando 10% a R${num} fica R${moeda.aumentar(num):.2f}')