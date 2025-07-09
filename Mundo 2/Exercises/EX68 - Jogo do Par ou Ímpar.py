# EX68 - Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
# ----------------------------------------------------------
print('======== EXERCÍCIO 68 ========')

import time
import random

computador = random.randint(1, 10)
nome = str(input('Olá, pequeno(a) gafanhoto(a)! Qual é seu nome? ')).strip()
print('-' * 80)
print(f"""Prazer em te conhecer {nome}! Esse é o "Jogo Par ou Ímpar,",
feito por Marco Caparra! Vamos lá?""")
print('-' * 80)
time.sleep(1.5)

jogador = int(input('Digite um valor inteiro: '))
pi = str(input('Você escolhe PAR ou ÍMPAR? [P/I] ')).strip().upper()[0]
print('-' * 80)
print('Carregando...')
soma = jogador + computador
sequencia = 0
print('-' * 80)
time.sleep(1.5)

while True:
    print(f"""Você jogou {jogador} e o computador {computador}.
Se somarmos essas valores, o resultado é {soma}. """, end = '')
    if soma % 2 == 0:
        print('Ou seja, deu PAR!')
        print('-' * 80)
        time.sleep(1)
        if pi == 'P':
            print('VOCÊ GANHOU!')
            print('-' * 80)
            sequencia += 1
        elif pi == 'I':
            print('VOCÊ PERDEU!')
            print('-' * 80)
            break

    if soma % 1 == 0:
        print('Ou seja, deu ÍMPAR!')
        print('-' * 80)
        time.sleep(1)
        if pi == 'P':
            print('VOCÊ PERDEU!')
            print('-' * 80)
            break
        elif pi == 'I':
            print('VOCÊ GANHOU!')
            print('-' * 80)
            sequencia += 1
    print('Vamos jogar novamente...')
    jogador = int(input('Digite um valor inteiro: '))
    pi = str(input('Você escolhe PAR ou ÍMPAR? [P/I] ')).strip().upper()[0]
print(f'Você conseguiu uma sequência de {sequencia} vítoria(s). Bom jogo, {nome}!')