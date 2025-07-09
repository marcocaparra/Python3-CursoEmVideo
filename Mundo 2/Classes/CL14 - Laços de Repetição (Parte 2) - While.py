# CL14 - Laços de Repetição (Parte 2) - While.
# ----------------------------------------------------------
print('======== AULA 14 - Laços de Repetição (Parte 2) - While ========')

# O laço de repetição while é um laço que executa enquanto uma condição for verdadeira.
# Ele é muito útil quando não sabemos quantas vezes precisamos repetir uma ação, ou quando queremos repetir uma ação até que uma condição seja satisfeita.

# While = Enquanto
# A sintaxe do while é a seguinte:
# while condição:
#     ação
# A identação é absolutamente necessária, pois é ela que define o que está dentro do laço de repetição e o que não está.

# Em Python, o while é usado da seguinte forma:
# while condição:
#     ação

# Exemplo:
contador = 0
while contador < 5:
    print('Contador:', contador)
    contador += 1

# No exemplo do chãozinho de Minecraft, como fizemos na aula 13, podemos usar o while para repetir a ação de colocar blocos até que o chão esteja completo.
# Vamos fazer isso agora:
# while not maça:
# if chão completo:
#     passo
# if buraco:
#     pule
# if moeda:
#     pegue
# pega

print('======== PARTE PRÁTICA ========')

n = 1
while n != 0:
    n = int(input('Digite aqui um número, e digite zero para acabar com o programa: '))
print('Você digitou zero, FIM!')

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite aqui algum número inteiro, e digite 0 para finalizar o programa: '))
    if n != 0:
        if n % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
print(f'FIM do programa! Você digitou {par} números pares, e {impar} números impares!')