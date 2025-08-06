def numeroParaTexto(numero):
    unidades = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
    dezenas = ['dez', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
    if 0 <= numero < 10:
        return unidades[numero]
    elif 10 <= numero < 100:
        return dezenas[numero // 10 - 1]
    elif 100 <= numero < 1000:
        return f"{unidades[numero // 100]} cento e {numeroParaTexto(numero % 100)}"
    else:
        return "Número fora do alcance"

def numeroParaTextoDecimal(numero):
    inteiro, decimal = str(numero).split('.')
    inteiro_texto = numeroParaTexto(int(inteiro))
    decimal_texto = ' '.join([numeroParaTexto(int(digito)) for digito in decimal])
    return f"{inteiro_texto} vírgula {decimal_texto}"

def numeroParaTextoMoeda(numero):
    if numero < 0:
        return "Valor negativo"
    elif numero == 0:
        return "zero reais"
    else:
        reais = int(numero)
        centavos = int((numero - reais) * 100)
        reais_texto = numeroParaTexto(reais)
        centavos_texto = numeroParaTexto(centavos)
        return f"{reais_texto} reais e {centavos_texto} centavos"