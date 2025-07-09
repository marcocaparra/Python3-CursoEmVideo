# EX62 - Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
# ----------------------------------------------------------
print('======== EXERCÍCIO 62 ========')

print('-'*20)
print('DEMONSTRAÇÃO RÁPIDA DE 10 TERMOS DE UMA PROGRESSÃO ARITMÉTICA')
print('-'*20)

primeiro = int(input('Digite aqui o primeiro termo dessa P.A: '))
razao = int(input('Digite aqui a razão dessa P.A: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + 10
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo = termo + razao
        cont = cont + 1
    print('PAUSE')
    mais = int(input('Mais quantos termos você quer que sejam mostrados? '))
print(f'O programa foi finalizado com sucesso, mostrando {total} termos!')
