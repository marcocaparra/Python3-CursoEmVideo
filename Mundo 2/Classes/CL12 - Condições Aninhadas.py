# CL12 - Condições Aninhadas.
# ----------------------------------------------------------
print('======== AULA 12 - Condições Aninhadas ========')

# Se chama "Aninhadas" porque uma condição pode estar dentro de outra.
# Agora, no exemplo de um carro na estrada, não temos só direita e esquerda, mas também temos a opção de seguir em frente ou parar.
# Aqui vai um exemplo como a da aula 11:
# carro.siga()
# se carro.esquerda(): -> if carro.esquerda():
    # carro.siga()
    # carro.direita()
    #carro.siga()
# senão se carro.direita(): -> elif carro.direita():
    # carro.siga()
    # carro.esquerda()
    # carro.direita()
    # carro.siga()
#senão: -> else:
    # carro.siga()
# carro.pare()

# Sempre precisamos de um if, mas podemos ter vários elif e um else no final.
# Ou as vezes, nem usamos o else, mas sempre precisamos de um if.

print('======== PARTE PRÁTICA ========')

nome = str(input('Digite seu nome: '))
if nome == 'Ana':
    print('Que nome bonito!') # Se o nome for Ana, imprime uma mensagem especial.

elif nome == 'Pedro' or nome == 'Maria':
    print('Seu nome é bem popular no Brasil!') # Se o nome for Pedro ou Maria, imprime uma mensagem diferente.

elif nome in 'João', 'José', 'Francisco', 'Antônio', 'Carlos':
    print('Seu nome é bem tradicional!') # Se o nome for um dos nomes tradicionais, imprime uma mensagem específica.

else:
    print('Seu nome é tão normal!') # Se o nome não for Ana, Pedro ou Maria, imprime uma mensagem genérica.
print(f'Bom dia, {nome}!')