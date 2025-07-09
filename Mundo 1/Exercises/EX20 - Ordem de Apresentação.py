# EX20 - O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
# ----------------------------------------------------------
print('======== EXERCÍCIO 20 ========')

import random
import time
aluno_1 = str(input("Olá, professor. Tudo bem? Digite aqui o PRIMEIRO aluno (dos 4) para fazer um sorteio de quem irá apagar o quadro: "))
aluno_2 = str(input("Digite aqui o SEGUNDO aluno (dos 4) para fazer um sorteio de quem irá apagar o quadro: "))
aluno_3 = str(input("Digite aqui o TERCEIRO aluno (dos 4) para fazer um sorteio de quem irá apagar o quadro: "))
aluno_4 = str(input("Digite aqui o QUARTO aluno (dos 4) para fazer um sorteio de quem irá apagar o quadro: "))
lista = [aluno_1, aluno_2, aluno_3, aluno_4]
random.shuffle(lista)
print(f"A ordem de apresentação será...")
time.sleep(2)
print(lista)