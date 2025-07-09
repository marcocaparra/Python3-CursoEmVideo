# CL10 - Condições.
# ----------------------------------------------------------
print('======== AULA 10 - Condições ========')

# Condições podem ser interpretadas como se um carro estivesse em um sinal vermelho ou verde.
    # Se o sinal estiver vermelho, o carro para. Se estiver verde, o carro anda.

# Estruturas sequenciais são executadas de forma linear, uma após a outra.
# Estruturas são comandos que serão fixos e outros que serão executados várias vezes. condicionais permitem que o programa tome decisões com base em condições específicas.
    # Terão comandos que serão fixos e outros que serão executados várias vezes.

# Condicionais
# if (se) - else (senão) - elif (senão se)
# Exemplo de condicional simples
# carro.siga()
# se carro.esquerda(): #if
#     carro.vire()
#     carro.siga()
#     carro.vire()
# senão: #else
#     carro.vire()
#     carro.siga()
# carro.pare()

# Blocos condicionais
# bloco True (verdadeiro) - bloco False (falso)
    # Dentro desses blocos, você pode colocar os comandos que deseja que sejam executados quando a condição for verdadeira ou falsa.

# Exemplo prático
tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Seu carro é novo.')
else:
    print('Seu carro é velho.')
print('--- Fim do programa ---')

print('======== PARTE PRÁTICA ========')

nome = str(input('Qual é seu nome: '))
if nome == 'Ana':
    print('Que nome lindo você tem!')
else:
    print('Que bosta de nome...')
print(f'Bom dia, {nome}!')
print('--- Fim do programa ---')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite aqui a segunda nota: '))
m = (n1 + n2/2)
print(f'A sua média foi {m:.1f}...')
if m >= 6.0:
    print('Parabéns pelo esforço!')
else:
    print('Que nota bosta, melhore...')