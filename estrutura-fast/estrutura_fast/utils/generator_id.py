from itertools import count

_contador = count(1)

def gerar_id():
    return next(_contador)

