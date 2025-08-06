# CL22 - Modularização.
# ----------------------------------------------------------
print('======== AULA 22 - Modularização ========')

# O conceito de modularização é muito importante na programação, pois permite dividir o código em partes menores e mais gerenciáveis.
# Esse conceito surgiu na época de 60, quando os computadores eram muito limitados em termos de memória e processamento.

import FUNC

num = int(input('Digite um número para calcular o fatorial: '))
fat = FUNC.fatorial(num)
print(f'O fatorial de {num} é {fat}')

# Vantagens da Modularização
# 1. Reutilização de Código: Funções podem ser reutilizadas em diferentes partes do programa.
# 2. Facilidade de Manutenção: Alterações em uma função não afetam o restante do código.
# 3. Melhoria na Legibilidade: Código modular é mais fácil de entender e seguir.
# 4. Testabilidade: Funções podem ser testadas individualmente, facilitando a identificação de erros.

print('======== PARTE PRÁTICA ========')

# Temos também os pacotes, que são coleções de módulos. Um pacote é um diretório que contém um arquivo especial chamado `__init__.py`, que indica que o diretório deve ser tratado como um pacote Python.

from uteis import numeros, data, cores

numero = int(input('Digite um número entre 0 e 999: '))
texto_numero = numeros.numeroParaTexto(numero)
print(f'O número {numero} por extenso é: {texto_numero}')
