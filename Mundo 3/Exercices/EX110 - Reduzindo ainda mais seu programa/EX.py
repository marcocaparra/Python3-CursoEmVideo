# EX109 - Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
# ----------------------------------------------------------
print('======== EXERCÍCIO 109 ========')

import moeda

num = float(input('Digite aqui um preço aleatório: R$'))
moeda.resumo(num, 80, 4)