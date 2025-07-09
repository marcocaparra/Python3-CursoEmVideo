# EX43 - Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo: IMC abaixo de 18,5: Abaixo do Peso. Entre 18,5 e 25: Peso Ideal. 25 até 30: Sobrepeso. 30 até 40: Obesidade. Acima de 40: Obesidade Mórbida.
# ----------------------------------------------------------
print('======== EXERCÍCIO 43 ========')

peso = float(input('Olá, usuário(a)! Digite aqui seu peso em kilogramas para calcular seu IMC e ver seu status: '))
altura = float(input('Show! Agora digite sua altura em metros: '))
imc = peso / (altura**2)

if imc < 18.5:
    print(f'Seu IMC é de {imc:.1f}, você está abaixo do peso.')
elif 18.5 <= imc < 25:
    print(f'Seu IMC é de {imc:.1f}, você está no peso ideal!')
elif 25 <= imc < 30:
    print(f'Seu IMC é de {imc:.1f}, você está com sobrepeso.')
elif 30 <= imc < 40:
    print(f'Seu IMC é de {imc:.1f}, você está com obesidade..')
else:
    print(f'Seu IMC é de {imc:.1f}, você está com obesidade mórbida...')