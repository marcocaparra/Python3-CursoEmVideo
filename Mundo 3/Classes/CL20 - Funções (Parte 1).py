# CL20 - Funções (Parte 1).
# ----------------------------------------------------------
print('======== AULA 20 - Funções (Parte 1) ========')

# A palavra "função" SEMPRE vai estar ligada a "ROTINA".
# Ou seja, sempre se pergunte as coisas que você faz SEMPRE que está programando.
# Funções, não é apenas o "def", mas também o "print", "input", "len", etc.

# Já que em todos exercícios, escrevemos linhas na tela, para personalizar o código, podemos criar uma função para isso.
def mostrarLinha():
    print('=' * 40)

mostrarLinha()
print('Aula 20 - Funções (Parte 1)')
mostrarLinha()

# Funções são ainda mais poderosas, pois podem receber parâmetros e retornar valores.
def mensagem(msg):
    print('=' * 40)
    print(msg)
    print('=' * 40)

mensagem('Aula 20 - Funções (Parte 1)')

print('======== PARTE PRÁTICA ========')

a = 4
b = 5
s = a + b
print(f'A soma de {a} + {b} é igual a {s}')
a = 8
b = 9
s = a + b
print(f'A soma de {a} + {b} é igual a {s}')
a = 2
b = 1
s = a + b
print(f'A soma de {a} + {b} é igual a {s}')

# Ou podemos criar uma função para isso, que recebe dois parâmetros e retorna o resultado da soma.

def soma(a, b):
    s = a + b
    print(f'A soma de {a} + {b} é igual a {s}')

soma(4, 5)
soma(8, 9)
soma(2, 1)

# Como o Python é uma linguagem moderna, podemos criar funções com parâmetros opcionais, chamadas "desacopamentos e acoplamentos"
def contador(*num):
    print('Contando...')
    for valor in num:
        print(f'{valor}, ', end='')
    print('Fim!')

contador(2, 3, 4, 7, 8)

# Caso na minha rotina, eu precise muito dobrar os valores de uma lista, posso criar uma função para isso.
def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1

valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(f'Os valores dobrados são: {valores}')

# Após aprendermos isso, podemos melhorar nossa função de soma...

def soma(*valores):
    s = 0
    for v in valores:
        s += v
    print(f'A soma dos valores {valores} é: {s}')

soma(4, 5)
soma(8, 9, 2, 1)