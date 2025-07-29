# CL16 - Tuplas.
# ----------------------------------------------------------
print('======== AULA 16 - Tuplas ========')

# AS TUPLAS SÃO IMUTÁVEIS!

# lanche = hamburguer

# lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)

# ou

print(lanche[0])
# e
print(lanche[0:2])
# e 
print(len(lanche))

# e também:
cont = 0
for c in lanche:
    cont =+ 1
    print(c)
        
print('======== PARTE PRÁTICA ========')

amor = ('MUITO', 'ABSURDAMENTE', 'INFINITAMENTE', 'PRA TODA VIDA')
for adjetivos in amor:
    print(f'Eu amo minha namorada (futura esposa) {adjetivos}!')

for cont in range(0, len(amor)):
    print(amor[cont])

for pos, amores in enumerate(amor):
    print(f'Eu amo {amores} a minha namorada, na posição {pos}')

print(sorted(amor))

print('EU AMO MINHA NAMORADA')

print('LITERALMENTE UM BOOBLESORT COM 2 LINHAS')
num = (98, 10, 34, 101)
print(sorted(num))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
loc = (c.index(4))
print(f'O número 4, aparece na posição {loc} da lista!')

del(amor)