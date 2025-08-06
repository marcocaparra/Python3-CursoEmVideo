def dataAtual():
    from datetime import datetime
    return datetime.now().strftime('%d/%m/%Y %H:%M:%S')

def dataFormatada(data):
    from datetime import datetime
    return datetime.strptime(data, '%d/%m/%Y %H:%M:%S').strftime('%d/%m/%Y %H:%M:%S')

def dataDiferenca(data1, data2):
    from datetime import datetime
    d1 = datetime.strptime(data1, '%d/%m/%Y %H:%M:%S')
    d2 = datetime.strptime(data2, '%d/%m/%Y %H:%M:%S')
    return abs((d2 - d1).days)

def dataParaTexto(data):
    from datetime import datetime
    d = datetime.strptime(data, '%d/%m/%Y %H:%M:%S')
    return d.strftime('%A, %d de %B de %Y %H:%M:%S')

def textoParaData(texto):
    from datetime import datetime
    return datetime.strptime(texto, '%A, %d de %B de %Y %H:%M:%S').strftime('%d/%m/%Y %H:%M:%S')