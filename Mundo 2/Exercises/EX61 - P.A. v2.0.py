# EX61 - Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
# ----------------------------------------------------------
print('======== EXERCÍCIO 61 ========')

print('-'*20)
print('DEMONSTRAÇÃO RÁPIDA DE 10 TERMOS DE UMA PROGRESSÃO ARITMÉTICA')
print('-'*20)

termo1 = int(input('Digite aqui o primeiro termo dessa P.A: '))
razao = int(input('Digite aqui a razão dessa P.A: '))
termo = termo1
c = 1
while c <= 10:
    print(f'{termo} -> ', end='')
    termo = termo + razao
    c = c + 1
print('FIM')
