import copy

def get_rango(octeto):
    inicio = copy.copy(octeto)
    fin = copy.copy(octeto)
    if type(octeto) is not list:
        inicio = [octeto]
        fin = [octeto]
    for x in range(4-len(inicio)):
        inicio.append("0")
        fin.append("255")
    return [".".join(inicio), ".".join(fin)]
