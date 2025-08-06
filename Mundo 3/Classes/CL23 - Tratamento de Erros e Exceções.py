# CL23 - Tratamento de Erros e Exceções.
# ----------------------------------------------------------
print('======== AULA 23 - Tratamento de Erros e Exceções ========')

# 'Expection' é um termo usado para descrever uma situação em que o programa encontra um erro ou uma condição inesperada durante a execução.
# Em Python, podemos usar o bloco try-except para tratar exceções e evitar que o programa seja interrompido abruptamente.

# 'try' e 'except' são usados para capturar e tratar exceções.

# Dentro do 'try' fica a operação que pode dar problema, e dentro do 'except' fica o que irá acontecer quando der falha...

# Além disso, colocamos um 'else' no que der certo! - VALE CITAR QUE É OPCIONAL, E NEM SEMPRE IRÉMOS USAR

# E por últimos, temos o 'finally', que ocorre independente da operação dar certo ou errado - E COMO O 'ELSE', É OPCIONAL



print('======== PARTE PRÁTICA ========')

try:
    a = float(input('Numerador: '))
    b = float(input('Denominador: '))
    r = a / b
    print('-' * 30)


except (ValueError, TypeError):
    print('Tivemos um problema com o tipo de dado que você digitou...')

except ZeroDivisionError:
    print('Não é possível dividir um número por zero...')

except KeyboardInterrupt:
    print('O usuário preferiu não digitar os dados...')

except Exception as Erro:
    print(f'Um erro ocorreu: {Erro}')

else:  
    print(f'O resultado é {r:.1f}')

finally:
    print(f'Volte sempre!')

