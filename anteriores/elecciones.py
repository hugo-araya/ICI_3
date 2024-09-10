def lee_votos(nombre):
    ent = open(nombre)
    coaliciones = []
    linea1 = ent.readline().rstrip('\n')
    linea2 = ent.readline().rstrip('\n')
    aux1 = linea1.split(';')
    for elem in aux1:
        aux2 = elem.split(':')
        aux3 = aux2[1].split('-')
        coaliciones.append([aux2[0], aux3])
    votos = linea2.split('$')
    return coaliciones, votos

def genera_partidos(coaliciones):
    pass

def contar_votos(partidos, votos):
    pass

def voto_x_coalicion(partidos, coaliciones):
    pass

def genera_salida(votos_coaliciones):
    pass

if __name__ == "__main__":
    coaliciones, votos = lee_votos('elecciones.txt')
    partidos = genera_partidos(coaliciones)
    partidos = contar_votos(partidos, votos)
    votos_coalicion = votos_x_coalicion(partidos, coaliciones)
    genera_salida(votos_coaliciones)

