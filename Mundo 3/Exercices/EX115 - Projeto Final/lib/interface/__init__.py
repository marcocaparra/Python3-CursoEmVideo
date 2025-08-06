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

def linha(tam = 42):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho('MENU PRINCIPAl')
    c = 1
    for i in lista:
        print(f'\033[33m{c} - \033[34m{i}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua opção: \033[m')
    return opc