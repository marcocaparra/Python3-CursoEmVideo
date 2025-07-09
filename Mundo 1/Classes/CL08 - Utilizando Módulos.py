# CL08 - Utilizando Módulos.
# ----------------------------------------------------------
print('======== AULA 8 - Utilizando Módulos ========')

# Módulos em Python são bibliotecas que contêm funções e variáveis que podem ser reutilizadas.
# Para utilizar um módulo, você deve importá-lo primeiro.
# Exemplo de importação de módulo:
import math  # Importa o módulo math, que contém funções matemáticas

# Para importar apenas uma função específica de um módulo, você pode usar:
from math import sqrt  # Importa apenas a função sqrt (raiz quadrada) do módulo
# Exemplo de uso do módulo math:
print(f"A raiz quadrada de 16 é {math.sqrt(16)}")  # Utiliza a função sqrt do módulo math

# Funções matemáticas comuns no módulo math:
from math import ceil # Arredonda para cima
from math import floor  # Arredonda para baixo
from math import trunc  # Trunca o número (remove a parte decimal)
from math import pow  # Eleva um número a uma potência
from math import sqrt # Calcula a raiz quadrada
from math import factorial  # Calcula o fatorial de um número

# Para importar duas funções específicas de um módulo, você pode usar:
from math import ceil, floor  # Importa as funções ceil e floor do módulo math

# Para encontrar todas as bibliotecas disponíveis em Python, você pode acessar a documentação oficial ou usar o comando `help('modules')` no console interativo do Python.

print('======== PARTE PRÁTICA ========')

'''import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print(f'A raiz quadrada de {num} é igual a {raiz:.2f}')'''

'''from math import sqrt
num = int(input('Digite um número: '))
raiz = sqrt(num)
print(f'A raiz quadrada de {num} é igual a {raiz:.2f}')'''

'''import random
num = random.randint(1, 10)  # Gera um número aleatório entre 1 e 10
print(f'O número aleatório gerado foi: {num}')'''

'''import time
time.sleep(2)  # Pausa a execução do programa por 2 segundos
print('Programa finalizado com sucesso!')'''

import emoji
print(emoji.emojize('Python is :thumbs_up:')) # Exibe um emoji de "curtir" com o texto "Python is 👍
print(emoji.emojize(f"Minha namorada é o {emoji.emojize(':red_heart:')}  da minha vida!"))  # Exibe o emoji de "curtir" com o texto "Python is 👍"
print(emoji.emojize('Turn down for what? :smiling_face_with_sunglasses:'))  # Exibe o emoji de "curtir" com o texto "Python is 👍"
# Para ver quais módulos externos estão instalados, você pode usar o comando `pip list` no terminal ou console do Python.