# EX04 - Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas informações sobre ele.
# ----------------------------------------------------------
print('======== EXERCÍCIO 4 ========')

carac = input("Digite algo do seu teclado: ")
print("Esse caracter é do tipo", type(carac))
print("Esse caracter é númerico ou alfabético?", carac.isalnum())
print("Esse caracter é apenas númerico?", carac.isnumeric())
print("Esse caracter é apenas alfabético?", carac.isalpha())
print("Esse caracter está apenas em letras maiúsculas?", carac.isupper())
print("Esse caracter está apenas em letras minúsculas?", carac.islower())
print("Esse caracter é apenas um espaço?", carac.isspace())
print("Esse caracter está capitalizado?", carac.istitle())