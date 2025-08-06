# EX113 - Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
# ----------------------------------------------------------
print('======== EXERCÍCIO 113 ========')

def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número INTEIRO VÁLIDO...\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mERRO! O usuário interrompeu a operação...\033[m')
            return 0
        else:
            return num


def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número REAL VÁLIDO...\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mERRO! O usuário interrompeu a operação...\033[m')
            return 0
        else:
            return num



n1 = leiaInt('Digite um número INTEIRO: ')
n2 = leiaFloat('Digite um número REAL: ')
print(f'O valor INTEIRO digitado foi "{n1}", e o REAL foi "{n2}"')