# EX104 - Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)
# ----------------------------------------------------------
print('======== EXERCÍCIO 104 ========')

def leiaNum(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número INTEIRO VÁLIDO!\033[m')
        if ok:
            break
    return valor

            
num = leiaNum('Digite um número: ')
print(f'Você acabou de digitar o número {num}: ')