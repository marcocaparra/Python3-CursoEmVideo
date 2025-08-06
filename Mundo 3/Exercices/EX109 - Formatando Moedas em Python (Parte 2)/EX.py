# EX109 - Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
# ----------------------------------------------------------
print('======== EXERCÍCIO 109 ========')

import moeda

num = float(input('Digite aqui um preço aleatório: R$'))
print(f'A metade de {moeda.moeda(num)} é {moeda.metade(num, True)}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.dobro(num, True)}')
print(f'Adicionando 10% de {moeda.moeda(num)} fica {moeda.aumentar(num, 10, True)}')
print(f'Reduzindo 15% de {moeda.moeda(num)} fica {moeda.diminuir(num, 15, True)}')