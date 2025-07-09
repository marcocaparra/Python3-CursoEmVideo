# CL15 - Interrompendo um While.
# ----------------------------------------------------------
print('======== AULA 15 - Interrompendo um While ========')

# O laço de repetição while pode ser interrompido a qualquer momento com o comando break.
# O break é um comando que interrompe o laço de repetição e sai dele imediatamente
# Ele é muito útil quando queremos sair de um laço de repetição antes que a condição seja satisfeita.

# A sintaxe do break é a seguinte:
# while condição:
#     ação
#     if condição_de_interrupção:
#         break

# Exemplo:
contador = 0
while contador < 5:
    print('Contador:', contador)
    contador += 1
    if contador == 3:
        break
print('O laço foi interrompido!')

# Podemos fazer um While infinito, que só será interrompido quando o usuário digitar um valor específico.
# Vamos fazer isso agora
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
print('FIM!')

print('======== PARTE PRÁTICA ========')

n = s = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    s += n
print(f'A soma dos números é: {s}')

# Pep: Uma proposta de melhoria do Python.