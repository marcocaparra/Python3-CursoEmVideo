# CL09 - Manipulando Textos.
# ----------------------------------------------------------
print('======== AULA 9 - Manipulando Textos ========')

# Manipulação de strings em Python é uma parte fundamental da linguagem.
# Strings são sequências de caracteres e podem ser manipuladas de várias maneiras.
# Letras maiúsculas, são diferentes de letras minúsculas, e Python é sensível a isso.
# Exemplo de criação de uma string:
texto = "Python é uma linguagem de programação versátil."

# Fatiamento de strings (slicing):
print(f"O sexto caractere da string é: {texto[5]}") # Acessa o sexto caractere
print(f"Os primeiros 6 caracteres da string são: {texto[:6]}")  # Acessa os primeiros 6 caracteres
print(f"Os caracteres a partir do 6 na string são: {texto[6:]}")  # Acessa a string a partir do índice 6 até o final
print(f"Os caracteres a partir do 6 na string com passo 3 são: {texto[6::3]}") # Acessa a string a partir do índice 6 com passo 3
print(f"A string toda com o passo 2 é: {texto[::2]}")  # Acessa a string toda com passo 2
print(f"Os últimos 6 caracteres da string são: {texto[-6:]}")  # Acessa os últimos 6 caracteres
print(f"Os caracteres do índice 2 ao 6 são: {texto[2:7]}")  # Acessa os caracteres do índice 2 ao 6
print(f"Os caracteres do índice 2 ao 6 com passo 2 são: {texto[2:7:2]}")  # Acessa os caracteres do índice 2 ao 6 pulando de 2 em 2

# Analise de strings:
print(f"O tamanho da string é: {len(texto)}")  # Retorna o tamanho da string
print(f"A string repete a letra 'a' {texto.count('a')} vezes.")  # Conta quantas vezes a letra 'a' aparece na string
print(f"A string repete a letra 'a' {texto.count('a', 0, 12)} vezes nos primeiros 12 caracteres.")  # Conta quantas vezes a letra 'a' aparece nos primeiros 12 caracteres
print(f"Foi encontrado a letra 'a' na posição: {texto.find('a')}")  # Retorna a posição da primeira ocorrência da letra 'a'
print(f"Não foi encontrado a letra 'z' na posição: {texto.find('z')}")  # Retorna -1 se não encontrar a letra 'z'
print(f"Foi encontrado a letra 'a' na string? {'a' in texto}")  # Verifica se a letra 'a' está na string

# Transformação de strings:
print(f"Na string, a palavra 'Python' vai ser substituída por 'Java': {texto.replace('Python', 'Java')}")  # Substitui a palavra 'Python' por 'Java'
print(f"A string em letras maiúsculas: {texto.upper()}")  # Converte a string para letras maiúsculas
print(f"A string em letras minúsculas: {texto.lower()}")  # Converte a string para letras minúsculas
print(f"Para deixar só o primeiro caractere em maiúsculo: {texto.capitalize()}")  # Converte o primeiro caractere para maiúsculo
print(f"Para deixar a primeira letra de cada palavra em maiúsculo: {texto.title()}")  # Converte a primeira letra de cada palavra para maiúsculo
frase_com_espacos = "   Python é uma linguagem de programação versátil.   "
print(f"Removendo os espaços no início e no final da string: {frase_com_espacos.strip()}")  # Remove os espaços no início e no final da string
print(f"Removendo os espaços no início da string: {frase_com_espacos.lstrip()}")  # Remove os espaços no início da string
print(f"Removendo os espaços no final da string: {frase_com_espacos.rstrip()}")  # Remove os espaços no final da string

# Divisão e junção de strings:
print(f"Dividindo a string em uma lista de palavras: {texto.split()}")  # Divide a string em uma lista de palavras a partir dos espaços
frase_teste = "Arroz com feijão é uma combinação deliciosa."
frase_teste_dividida = frase_teste.split()  # Divide a string em uma lista de palavras
print(f"{frase_teste_dividida[0] [2]}") # Acessa o terceiro caractere da primeira palavra da lista
print(f"Juntando a lista de palavras em uma string: {'-'.join(texto.split())}")  # Junta a lista de palavras em uma string com hífens

# Para colocar um texto grande em várias linhas, podemos usar três aspas simples ou duplas:
print("""
Para colocar um texto grande em várias linhas,
podemos usar três aspas simples ou duplas:
""")

