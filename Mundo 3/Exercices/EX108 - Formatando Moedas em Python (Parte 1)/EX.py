# EX107 - Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.
# ----------------------------------------------------------
print('======== EXERCÍCIO 108 ========')

import moeda

num = float(input('Digite aqui um preço aleatório: R$'))
print(f'A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}')
print(f'Adicionando 10% a {moeda.moeda(num)} fica {moeda.moeda(moeda.aumentar(num, 10))}')