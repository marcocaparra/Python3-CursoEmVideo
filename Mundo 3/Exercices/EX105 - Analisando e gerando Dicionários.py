# EX105 - Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações
# ----------------------------------------------------------
print('======== EXERCÍCIO 105 ========')

def dadosNotas(*nota, sit):
    '''
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    '''
    dados = {}
    dados['Total'] = len(nota)
    dados['Maior Nota'] = max(nota)
    dados['Menor Nota'] = min(nota)
    dados['Média das Notas'] = sum(nota)/len(nota)
    if sit:
        if dados['Média das Notas'] >= 7:
            dados['Situação'] = 'APROVADO'
        if dados['Média das Notas'] >= 5:
            dados['Situação'] = 'RAZOÁVEL'
        else:
            dados['Situação'] = 'RUIM'
    return dados

resp = dadosNotas(1.5, 2.5, 8.5, sit=True)
print(resp)
help(dadosNotas)