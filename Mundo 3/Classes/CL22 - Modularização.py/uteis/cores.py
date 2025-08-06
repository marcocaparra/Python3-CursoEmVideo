def textoParaCor(texto, cor):
    cores = {
        'vermelho': '\033[31m',
        'verde': '\033[32m',
        'amarelo': '\033[33m',
        'azul': '\033[34m',
        'magenta': '\033[35m',
        'ciano': '\033[36m',
        'branco': '\033[37m',
    }
    return f"{cores.get(cor, '\033[37m')}{texto}\033[0m"

def textoParaCorFundo(texto, cor):
    cores_fundo = {
        'vermelho': '\033[41m',
        'verde': '\033[42m',
        'amarelo': '\033[43m',
        'azul': '\033[44m',
        'magenta': '\033[45m',
        'ciano': '\033[46m',
        'branco': '\033[47m',
    }
    return f"{cores_fundo.get(cor, '\033[47m')}{texto}\033[0m"

def textoParaEstilo(texto, estilo):
    estilos = {
        'negrito': '\033[1m',
        'italico': '\033[3m',
        'sublinhado': '\033[4m',
        'tachado': '\033[9m',
    }
    return f"{estilos.get(estilo, '')}{texto}\033[0m"