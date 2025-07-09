# CL13 - Laços de Repetição (Parte 1).
# ----------------------------------------------------------
print('======== AULA 13 - Laços de Repetição (Parte 1) ========')

# Serve para evitar que nós fiquemos repetindo várias vezes uma ação.
# Num exemplo claro, se nós tivermos vários bloquinhos de código que se repetem, nós podemos usar um laço de repetição para evitar a repetição do código.

# Isso escrito em protuguês, como código, ficaria assim:
# laco c no intervalo(1,10):
#   passo
# pega

# Em inglês, isso seria:
# for c in range(1,10):
#  passo
# pegar

# A identação aqui é absolutamente necessária, pois é ela que define o que está dentro do laço de repetição e o que não está.

# E também vemos mais estruturas aninhadas, pois podemos ter condições dentro de laços de repetição, e laços de repetição dentro de laços de repetição.
# Como no exemplo (em português) abaixo:
# laco c no intervalo(1,10):
#   se c % 2 == 0:
#     passo
# pega

print('======== PARTE PRÁTICA ========')

import time

for c in range(1, 11): # <--- Aqui estamos contando de 1 até 10
    print(f'Contando: {c}') # <--- Aqui estamos imprimindo o número atual da contagem
    time.sleep(1) # <--- Aqui estamos fazendo uma pausa de 1 segundo entre cada número impresso
print('Cheguei ao final do laço!') # <--- Aqui estamos imprimindo uma mensagem final após o término do laço

# Caso quissessemos contar de 10 até 0, poderíamos fazer assim:
for c in range(10, -1, -1): # <--- Aqui estamos contando de 10 até 0
    print(f'Contando: {c}') # <--- Aqui estamos imprimindo o número atual da contagem
    time.sleep(1) # <--- Aqui estamos fazendo uma pausa de 1 segundo entre cada número impresso
print('Cheguei ao final do laço!') # <--- Aqui estamos imprimindo uma mensagem final após o término do laço

n = int(input('Digite um número: ')) # <--- Aqui estamos pedindo ao usuário para digitar um número
for c in range(1, n + 1): # <--- Aqui estamos contando de 1 até o número digitado pelo usuário
    print(f'Contando: {c}') # <--- Aqui estamos imprimindo o número atual da contagem
    time.sleep(1) # <--- Aqui estamos fazendo uma pausa de 1 segundo entre cada número impresso
print('Cheguei ao final do laço!') # <--- Aqui estamos imprimindo uma mensagem final após o término do laço

i = int(input('Início: ')) # <--- Aqui estamos pedindo ao usuário para digitar o início da contagem
f = int(input('Fim: ')) # <--- Aqui estamos pedindo ao usuário para digitar o fim da contagem
p = int(input('Passo: ')) # <--- Aqui estamos pedindo ao usuário
for c in range(i, f + 1, p): # <--- Aqui estamos contando do início ao fim com o passo definido pelo usuário
    print(f'Contando: {c}') # <--- Aqui estamos imprimindo o número
    time.sleep(1) # <--- Aqui estamos fazendo uma pausa de 1 segundo entre cada número impresso
print('Cheguei ao final do laço!') # <--- Aqui estamos imprimindo uma mensagem final após o término do laço

s = 0 # <--- Aqui estamos inicializando uma variável para somar os números
for c in range(1, 4): # <--- Aqui estamos contando de 1 até 3
    n = int(input(f'Digite o {c}º número: ')) # <--- Aqui estamos pedindo ao usuário para digitar um número
    s += n # <--- Aqui estamos somando o número digitado pelo usuário à variável s
print(f'A soma dos números é: {s}') # <--- Aqui estamos imprimindo a soma dos números