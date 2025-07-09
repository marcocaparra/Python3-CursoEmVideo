# EX37 - Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
# ----------------------------------------------------------
print('======== EXERCÍCIO 37 ========')

num = int(input('Digite aqui um número inteiro, para usar nosso conversor: '))
print("""Escolha uma das bases para conversão:
[ 1 ] - Conversão para Binário
[ 2 ] - Conversão para Octal
[ 3 ] - Conversão para Hexadecimal""")
opcao = int(input("Digite aqui sua opção: "))
if opcao == 1:
    print(f"O número inteiro {num} convertido para binário é: {bin(num)[2:]}!")
elif opcao == 2:
    print(f'O número inteiro {num} convertido para octal é: {oct(num)[2:]}!')
elif opcao == 3:
    print(f'O número inteiro {num} convertido para hexadecimal é: {hex(num)[2:]}!')
else:
    print('Você não escolheu a opção 1, 2 ou 3... Reinicie o programa e tente novamente.')