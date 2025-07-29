# EX92 - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
# ----------------------------------------------------------
print('======== EXERCÍCIO 92 ========')

from datetime import datetime

dados = {}

dados['Nome'] = str(input('Digite aqui o seu nome: ')).strip()
dados['Ano de Nascimento'] = int(input('Digite aqui o ano em que você nasceu: '))
dados['CLT'] = int(input('''Digite aqui a sua CTPS (na Carteira de Trabalho). 
Caso você não tenha, DIGITE 0: '''))

if dados['CLT'] == 0:
    print('-=' * 30)

    print(f'O seu nome é {dados["Nome"]}.')
    print(f'Você tem {datetime.now().year - dados["Ano de Nascimento"]} anos.')
    print(f'Você um trabalhador(a) (ou ainda vai ser) NÃO registrado(a).')

else:
    dados['Ano de Contratação'] = int(input('Qual foi o ano da sua contratação? '))
    dados['Salário'] = float(input('Certo. E qual é seu salário atual? '))

    print('-=' * 30)

    print(f'O seu nome é {dados["Nome"]}.')
    print(f'Você tem {datetime.now().year - dados["Ano de Nascimento"]} anos.')
    print(f'Sua CTPS possui o número {dados["CLT"]}.')
    print(f'Você foi contratado(a) em {dados["Ano de Contratação"]}.')
    print(f'O seu salário atual é de {dados["Salário"]:.2f}.')
    print(f'O esperado é que você se aposente com: {(datetime.now().year - dados['Ano de Nascimento']) + (dados["Ano de Contratação"] + 35) - datetime.now().year} anos.')