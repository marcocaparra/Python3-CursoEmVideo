# EX97 - Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
# ----------------------------------------------------------
print('======== EXERCÍCIO 97 ========')

def escreva(msg):
    tam = len(msg) + 4
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)

escreva('Curso em Vídeo - Python')