# EX102 - Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
# ----------------------------------------------------------
print('======== EXERCÍCIO 102 ========')

def fatorial(num, show):
    f = 1
    for n in range(num, 0, -1):
        f *= n
    if show == False:
        return f'O fatorial de {num} é: {f}'
    if show == True:
        print(f'Certo! O cálculo para o fatorial de {num} é:')
        for n in range(num, 0, -1):
            print(n, end='')
            if n > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= n
        return f
            

num = int(input('Digite aqui um número para calcular seu fatorial: '))

while True:
    show = str(input(f'Deseja ver a conta que será feita para calcular o fatorial de {num}? ')).upper()[0]
    if show in 'SN':
        break
    print('ERRO! Digite apenas S ou N...')
if show == 'S':
    show = True 
elif show == 'N':
    show = False

print('-=' * 30)
print(fatorial(num, show))