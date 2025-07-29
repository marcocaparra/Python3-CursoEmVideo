# EX74 - Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
# ----------------------------------------------------------
print('======== EXERCÍCIO 74 ========')

import random
n1 = random.randint(1, 10)
n2 = random.randint(1, 10)
n3 = random.randint(1, 10)
n4 = random.randint(1, 10)
n5 = random.randint(1, 10)
n = (n1, n2, n3, n4, n5)

print(f'O computador pensou nos números: {n}')
print('-' * 20)
print(f'O maior número entre eles {max(n)}')
print('-' * 20)
print(f'O menor número entre eles é {min(n)}')