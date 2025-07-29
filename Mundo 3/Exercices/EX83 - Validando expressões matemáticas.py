# EX83 - Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
# ----------------------------------------------------------
print('======== EXERCÍCIO 83 ========')

expr = str(input('Digite a sua expressão matemática: '))
pilha = []
for s in expr:
    if s == '(':
        pilha.append('(')
    elif s == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('A sua expressão está válida!')
else:
    print('A sua expressão está inválida.')