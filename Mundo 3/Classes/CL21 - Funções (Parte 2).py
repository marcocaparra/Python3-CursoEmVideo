# CL21 - Funções (Parte 2).
# ----------------------------------------------------------
print('======== AULA 21 - Funções (Parte 2) ========')

# Interactive Help
    # O 'Interactive Help' é uma ferramenta que permite ao usuário obter informações sobre funções, módulos, classes e outros objetos do Python diretamente no console.
'''help(len)
help(print)
help(input)
help(str)
import datetime
help(datetime)
    # Ou podemos usar o método __doc__ para obter a documentação de um objeto.
print(len.__doc__)
print(print.__doc__)
print(input.__doc__)
print(str.__doc__)
print(datetime.__doc__)'''

# Docstrings
    # As 'Docstrings' são strings de documentação que descrevem o propósito e o uso de uma função, classe ou módulo. Elas são escritas logo após a definição do objeto e podem ser acessadas usando o atributo `__doc__`.
def contador(i, f, p):
    """
    Faz uma contagem de i até f de p em p.
    :param i: Início da contagem.
    :param f: Fim da contagem.
    :param p: Passo da contagem.
    Função criada por: Marco Caparra
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('Fim!')

# Parametros Opcionais
    # Parâmetros opcionais são aqueles que não precisam ser fornecidos quando a função é chamada. Se não forem fornecidos, eles assumem um valor padrão definido na função.
def somar(a=0, b=0):
    """
    Faz a soma de a e b.
    :param a: Primeiro valor.
    :param b: Segundo valor.
    :return: A soma de a e b.
    """
    return a + b
print(somar(5, 2))  # Saída: 7
print(somar(5))     # Saída: 5 (b assume o valor padrão)
print(somar())      # Saída: 0 (a e b assumem o valor padrão)

# Escopo de Variáveis
    # O escopo de variáveis refere-se à região do código onde uma variável é acessível. Em Python, as variáveis podem ter escopo local (dentro de uma função) ou global (fora de todas as funções).
x = 10  # Variável global
def funcao():
    y = 5  # Variável local
    print(x)  # Acessando a variável global
    print(y)  # Acessando a variável local
funcao()
'''print(y)''' # Isso causará um erro, pois y não está definido no escopo global
    # Cuidado ao criar uma variável local com o mesmo nome de uma variável global, pois irá ser criado uma variável local, que não será a mesma que a global.
def funcao2():
    x = 20  # Variável local com o mesmo nome da variável global
    print(x)  # Acessando a variável local
funcao2()
print(x)  # Acessando a variável global, que ainda é 10
    # Mas podemos usar a palavra-chave `global` para modificar uma variável global dentro de uma função.
def funcao3():
    global x  # Declarando que queremos usar a variável global x
    x = 30  # Modificando a variável global
    print(x)  # Acessando a variável global modificada

# Retorno de Valores
    # Uma função pode retornar um valor usando a palavra-chave `return`.
def quadrado(n):
    return n ** 2
print(quadrado(5))  # Saída: 25

print('======== PARTE PRÁTICA ========')

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input('Digite um número: '))
print(f'O fatorial do número {n} é {fatorial(n)}!')

def par(num=0):
    if num % 2 == 0:
        return True
    else:
        return False
    
num = int(input('Digite um número: '))
par(num)
if par(num) == True:
    print('É PAR!')
else:
    print('É ÍMPAR!')