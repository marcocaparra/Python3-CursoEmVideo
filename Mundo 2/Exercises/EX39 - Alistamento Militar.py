# EX39 - Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
# ----------------------------------------------------------
print('======== EXERCÍCIO 39 ========')

idade = int(input('Olá, jovem. Digite aqui sua idade: '))
prazo = idade - 18
falta = 18 - idade

if idade < 18:
    print(f'Ainda falta(m) {falta} anos para você poder se alistar...')
elif idade == 18:
    print(f'Jovem, esse é o momento exato onde você deve se alisar!')
elif idade > 18:
    print(f'O prazo para seu alistamento já foi a {prazo} ano(s).')
print('Obrigado por usar o nosso programa de alistamento!')
