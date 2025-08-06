# EX114 - Crie um código em Python que teste se o site pudim está acessível pelo computador usado. um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
# ----------------------------------------------------------
print('======== EXERCÍCIO 114 ========')

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('O site "Pudim" NÃO está acessível no momento :(')
else:
    print('O site "Pudim" ESTÁ acessível no momento :)')