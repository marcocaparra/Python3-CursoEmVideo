# CL11 - Cores no Terminal.
# ----------------------------------------------------------
print('======== AULA 11 - Cores no Terminal ========')

# Cores no terminal
# ANSI Escape Codes
print('\033[0;30m Preto \033[m')
print('\033[0;31m Vermelho \033[m')
print('\033[0;32m Verde \033[m')
print('\033[0;33m Amarelo \033[m')
print('\033[0;34m Azul \033[m')
print('\033[0;35m Roxo \033[m')
print('\033[0;36m Cyan \033[m')
print('\033[0;37m Branco \033[m')

# Estilos de texto
print('\033[1;30m Negrito \033[m')
print('\033[4;30m Sublinhado \033[m')
print('\033[7;30m Invertido \033[m')

# Cores de fundo
print('\033[40;30m Fundo Preto \033[m')
print('\033[41;30m Fundo Vermelho \033[m')

# Cores de texto e fundo combinadas
print('\033[1;31;40m Vermelho em Preto \033[m')
print('\033[1;32;41m Verde em Vermelho \033[m')
print('\033[1;33;42m Amarelo em Verde \033[m')

# Resetando as cores
print('\033[m Texto normal')

# Cores com variáveis
cores = {
    'limpa': '\033[m',
    'azul': '\033[0;34m',
    'amarelo': '\033[0;33m',
    'verde': '\033[0;32m',
    'vermelho': '\033[0;31m',
    'roxo': '\033[0;35m',
    'ciano': '\033[0;36m',
    'branco': '\033[0;37m'
}

print(f'{cores["azul"]}Texto em azul{cores["limpa"]}')